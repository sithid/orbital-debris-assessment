# All utility functions should have complete docstrings for clarity and maintainability.
# All utility functions that were assisted by AI have 'AI Assisted Function' in comment headers for easy identification.
import pandas as pd
import numpy as np
import sqlite3 as sql
from IPython.display import display, Markdown 

# Various constants for calculations.
earth_radius = 6378.137
mu = 398600.4418 # Earth's gravitational parameter (km^3/s^2)

def calculate_dry_mass(row):
    """
    Estimate the dry mass of a satellite based on its wet mass, object type, and orbital regime.

    Parameters:
    row (pd.Series): A row from the satellite DataFrame containing 'proxy_mass_kg', 'object_type', and 'orbit_class'.

    Returns:
    float: The estimated dry mass in kilograms.
    """
    wet_mass = row['proxy_mass_kg']
    obj_type = row['object_type']
    regime = row['orbit_class']
    
    # Station-Keeping: The act of maintaining a satellite's orbit.
    # Typically requires small amounts of fuel for minor adjustments to keep
    # the satellite in its intended orbit. Satellites are affected by a variety
    # of external factors requiring periodic thruster adjustments.

    # Debris and Rocket Bodies are essentially dry structures (no fuel)
    if obj_type in ['DEBRIS', 'ROCKET BODY']:
        return wet_mass 
    
    # Payloads follow orbit-specific fuel-fraction logic
    if obj_type == 'PAYLOAD':
        if regime == 'LEO':
            # LEO satellites typically carry minimal fuel (<10%). They get carried into
            # orbit by a launch vehicle and use small propulsion for station-keeping.
            # Conservative estimate: 90% Dry Mass.
            return wet_mass * 0.90
        else:
            # GEO/MEO/Deep Space satellites often require significant fuel reserves
            # to reach and maintain their orbits, as well as for station-keeping maneuvers
            # Standard estimate: 55% Dry Mass.
            return wet_mass * 0.55
            
    return wet_mass

# Derive user_category PER OBJECT using a three-tier priority:
#    Tier 1: Per-row boolean flags (from UCS data — most accurate for matched payloads)
#    Tier 2: Per-row users text (UCS free text for matched payloads)
#    Tier 3: Owner-level mode-based category fallback (for SATCAT-only debris/rocket bodies)
# We only need this because I broke the flags previously by using max() in aggregation, which caused is_commercial = 1 to bleed across
# mixed-sector owner codes like 'US'. This made query results unreliable and inconsistent with UCS data for matched payloads. 
def derive_user_category(row, map):
    # Tier 1: per-object boolean flags
    if row['is_commercial'] == 1: return 'COMMERCIAL'
    if row['is_government'] == 1: return 'GOVERNMENT'
    if row['is_military']   == 1: return 'MILITARY'
    if row['is_civil']      == 1: return 'CIVIL'
    
    # Tier 2: per-object users text
    users = str(row['users'] if pd.notna(row['users']) else '').strip().upper()
    
    if users:
        if 'MILITARY'   in users: return 'MILITARY'
        if 'GOVERNMENT' in users: return 'GOVERNMENT'
        if 'CIVIL'      in users: return 'CIVIL'
        if 'COMMERCIAL' in users: return 'COMMERCIAL'
        
    # Tier 3: owner-level fallback
    return map.get(str(row['owner_code']).strip().upper(), 'UNKNOWN')

# Priority: MILITARY > GOVERNMENT > CIVIL > COMMERCIAL > UNKNOWN
def category_from_users_text(users_text):
    if pd.isna(users_text) or str(users_text).strip() == '':
        return 'UNKNOWN'
    
    u = str(users_text).upper()
    
    if 'MILITARY'   in u: return 'MILITARY'
    if 'GOVERNMENT' in u: return 'GOVERNMENT'
    if 'CIVIL'      in u: return 'CIVIL'
    if 'COMMERCIAL' in u: return 'COMMERCIAL'
    return 'UNKNOWN'

def categorize_rcs(val):
    """
    Categorize the radar cross-section (RCS) value into size classes.

    Parameters:
    val (float): The RCS value in square meters.

    Returns:
    str: The size category ('UNKNOWN', 'SMALL', 'MEDIUM', 'LARGE').
    """
    if pd.isna(val): return 'UNKNOWN'
    elif val < 0.1:    return 'SMALL'
    elif val < 1.0:    return 'MEDIUM'
    else: return 'LARGE'

def derive_category(row):
    """
    Derive the category of a space object based on its type and status.

    Parameters:
    row (pd.Series): A row from the satellite DataFrame.

    Returns:
    str: The category of the space object.
    """
    if row['object_type'] == 'DEBRIS': return 'Debris'
    elif row['object_type'] == 'ROCKET BODY': return 'Rocket Body'
    elif row['object_type'] == 'PAYLOAD':
        return 'Inactive Satellite' if row['is_zombie'] == 1 else 'Active Satellite'
    return 'Unknown'

def fill_power_smart(row, odm, gdm):
    """
    Fill power consumption for satellites based on available data and object type.

    Parameters:
    row (pd.Series): A row from the satellite DataFrame.
    odm (dict): Orbit-dependent power ratios.
    gdm (float): Global default power ratio.

    Returns:
    float: Imputed power consumption in watts.
    """
    if pd.notna(row['proxy_power_watts']):
        return row['proxy_power_watts']
    
    if row['object_type'] == 'PAYLOAD':
        mass = row['proxy_mass_kg']
        orbit = row['orbit_class']
        
        if pd.isna(orbit):
            ratio = gdm
        else:
            ratio = odm.get(orbit, gdm)
        
        return mass * ratio
    
    return 0.0

def load_query_result(query_name):
    """
    Load query results from a parquet file for a given query.
    
    Parameters:
    query_name (str): The name of the query whose results are to be loaded.
    
    Returns:
    pd.DataFrame: The query results as a pandas DataFrame.
    """
    file_path = f'../data/clean/results/{query_name}.parquet'
    return pd.read_parquet(file_path)

def run_query(sql, conn):
    """
    Execute a SQL query and return the results as a pandas DataFrame.
    
    Parameters:
    sql (str): The SQL query to be executed.
    conn (sql.Connection): The database connection object.
    
    Returns:
    pd.DataFrame: The results of the SQL query as a pandas DataFrame.
    """
    return pd.read_sql(sql, conn)

# Standardize Primary Purpose (Mission)
def standardize_purpose(text):
    if pd.isna(text) or text == 'Unknown':
        return 'Unknown'
    
    # Take the first primary term if there are multiple.
    primary = text.split('/')[0].strip()
    
    mapping = {
        'Earth Science': 'Earth Observation',
        'Meteorological': 'Earth Observation',
        'Surveillance': 'Earth Observation',
        'Earth': 'Earth Observation',
        'Earth/Space Observation': 'Earth Observation',
        'Space Observation': 'Space Science',
        'Technology Demonstration': 'Technology Development',
        'Mission Extension Technology': 'Technology Development',
        'Platform': 'Technology Development',
        'Satellite Positioning': 'Navigation',
        'Navigation': 'Navigation',
        'Communications': 'Communications',
        'Space Science': 'Space Science',
        'Educational': 'Educational'
    }
    
    # dict.get( p1, p2 )
    # where p1: the key to look up in the dictionary (in this case, the primary purpose term)
    # and p2: the default value to return if the key is not found in the dictionary (in this case, the original primary term)

    return mapping.get(primary, primary)

def classify_risk_category(
    row,
    ke_col="kinetic_joules",
    mass_col="proxy_mass_kg",
    thresholds=None,
    mass_cutoff=1.0,
    use_mass_filter=True
):
    """
    Classify orbital debris or satellite risk category based on kinetic energy and (optionally) mass.

    Parameters:
    row (pd.Series): Row of DataFrame with at least kinetic energy and mass columns.
    ke_col (str): Name of the kinetic energy column (default 'kinetic_joules').
    mass_col (str): Name of the mass column (default 'proxy_mass_kg').
    thresholds (dict or None):
        Ordered mapping of {category: min_ke_joules}. Example (descending):
            {
                'Extremely High Risk': 1e10,
                'High Risk': 1e8,
                'Moderate Risk': 1e6,
                'Low Risk': 0
            }
        If None, uses NASA/ESA-aligned defaults.
    mass_cutoff (float): Minimum mass (kg) to be considered for risk (default 1.0 kg).
    use_mass_filter (bool): If True, objects below mass_cutoff are always 'Low Risk'.

    Returns:
    str: Risk category label.

    Notes:
    - Designed for DataFrame.apply(axis=1) usage.
    - Defaults are based on NASA/ESA MMOD and kinetic energy risk guidelines.
    - Set use_mass_filter=False to ignore mass in risk assignment.
    """
    # Default thresholds (descending order)
    if thresholds is None:
        thresholds = {
            'Extremely High Risk': 1e10,
            'High Risk': 1e8,
            'Moderate Risk': 1e6,
            'Low Risk': 0
        }

    ke = row.get(ke_col, np.nan)
    mass = row.get(mass_col, np.nan)

    if pd.isna(ke):
        return 'Unknown'

    # If use_mass_filter is True, filter out very small objects as always low risk
    if use_mass_filter and (pd.isna(mass) or mass < mass_cutoff):
        return 'Low Risk'

    for category, min_ke in thresholds.items():
        if ke >= min_ke:
            return category
        
    return 'Low Risk'
    
def classify_orbit(period):
    """
    Translates orbital period into standardized regimes.

    Parameters:
    period (float): The orbital period in minutes. Period is a key parameter that can be used to classify the orbital regime of a satellite.

    Returns:
    str: The classified orbital regime ('LEO', 'MEO', 'GEO', 'Elliptical', or 'UNKNOWN').
    """
    if pd.isnull(period) or period <= 0:
        return 'UNKNOWN'
    elif period < 128:
        return 'LEO'
    elif 1400 <= period <= 1460:
        return 'GEO'
    elif 128 <= period < 1400:
        return 'MEO'
    else:
        return 'Elliptical'
    
# Used in 04_orbital_debris_synthesis.ipynb to get the first non-null, non-empty value from a series
# for aggregation of multiple columns. Strips whitespace and treats empty strings as 
# nulls as well.  This is a common pattern in the data where multiple columns may have the same
# underlying value but with different formatting, and we want to get the first valid one.
def first_non_null(series):
    """
    Return the first non-null, non-empty value from a pandas Series.

    Parameters:
    series (pd.Series): The input pandas Series.

    Returns:
    The first non-null, non-empty value from the series, or None if no such value exists.
    """

    # Drop nulls, return None if the series is empty after.
    s = series.dropna()
    if s.empty:
        return None
    
    # Strip whitespace and filter out empty strings.
    s = s.astype(str).str.strip()
    s = s[s != '']

    # Return the first valid value or None if none exist.
    return s.iloc[0] if not s.empty else None

def map_payload_status(value):
    if value == 'OPERATIONAL':
        return 'OPERATIONAL'
    if value == 'NON-OPERATIONAL':
        return 'NON-OPERATIONAL'
    if value == 'UNKNOWN':
        return 'UNKNOWN'
    return 'OTHER'

def map_lifecycle_status(row):
    if row['in_orbit'] == 1:
        return 'IN_ORBIT'
    if row['in_orbit'] == 0 or pd.notna(row['decay_date']):
        return 'DECAYED'
    return 'UNKNOWN'
        
def quick_report(df, title="Dataset Diagnostic", audit_cols=None, key_col=None):
    """
    This report focuses on the core stats and simple data quality indicators, without getting into complex analysis or visualizations.
    It is designed to be a quick check of the dataset's health and structure.
    """
    # Basic Stats
    rows, cols = df.shape
    mem_usage = df.memory_usage(deep=True).sum() / 1024**2

    # Build the report header
    report = [
        f"# {title}\n",
        f"**Dimensions:** {rows:,} rows × {cols} columns\n",
        f"**Memory Footprint:** {mem_usage:.2f} MB\n",
    ]

    # duplicate key audit if key_col is provided and exists in df
    if key_col and key_col in df.columns:
        dup_count = df.duplicated(subset=[key_col]).sum()
        
        if dup_count == 0:
            report.append(f"**Primary Key Check**: ✅ No duplicate {key_col} values detected\n")
        else:
            report.append(f"**Primary Key Check**: ⚠️ {dup_count:,} duplicate {key_col} values detected\n")
    
    report += [
        "\n---",
        "### 📊 Data Quality Audit",
        "| Column | Type | Nulls | Fill % | Status |",
        "| :--- | :--- | :--- | :--- | :--- |"
    ]

    # If no columns specified, use all columns
    target_cols = audit_cols if audit_cols else df.columns

    # Analyze each column for null counts, fill rates, and data types
    for col in target_cols:
        null_count = df[col].isna().sum()
        fill_rate = (rows - null_count) / rows
        dtype = str(df[col].dtype)
        status = "✅" if fill_rate > 0.8 else "⚠️"
        
        row_str = f"| **{col}** | `{dtype}` | {null_count:,} | {fill_rate:.1%} | {status} |"
        report.append(row_str)

    # Add a quick object summary if any object columns exist
    objs = df.select_dtypes(include='object')
    if not objs.empty:
        report.append("\n### 📝 Object Overview")
        report.append(objs.describe().T.to_markdown())

    # Add a quick numeric summary if any numeric columns exist
    nums = df.select_dtypes(include='number')
    if not nums.empty:
        report.append("\n### 📈 Numeric Overview")
        report.append(nums.describe().T.to_markdown())

    # Join list into a single string and display
    return display(Markdown("\n".join(report)))

#########################################################################################################
# AI Assisted Function: calculate_orbital_period                                                        #
#                                                                                                       #
# What this does                                                                                        #
# - Calculates orbital period using Kepler's Third Law when period is missing.                          #
# - Uses the formula: T = 2 * pi * sqrt(a^3 / mu), where T is the orbital period in seconds,            #
#   a is the semi-major axis in kilometers, and mu is Earth's gravitational parameter.                  #
# - Accounts for Earth's radius to convert altitudes to distances from Earth's center.                  #
#                                                                                                       #
# How AI assistance was used                                                                            #
# - I understand the concept of orbital period, and how to use it to derive orbital regime,             #
#   but I wasn't sure of the formula to use, the function itself is straightforward once the            #
#   formula is known.  AI provided the formula for orbital period, I provided the implementation.       #
#                                                                                                       #
# AI (GitHub Copilot, Various Models) assisted with formula reconstruction.                              #
#########################################################################################################
def calculate_orbital_period(row):
    """
    Calculate orbital period using Kepler's Third Law when period is missing.

    This helper function was rewritten to support both raw source columns and the normalized snake_case
    schema used later in the cleaning pipelines. This allows the function to be used anywhere within any of the cleaning pipelines
    without needing to modify it for different column naming conventions.

    Parameters:
    row (pd.Series): A row containing period, perigee, and apogee values.

    Returns:
    float: The existing period when available, the reconstructed period in
    minutes when enough geometry is present, or np.nan if reconstruction is
    not possible.
    """
    
    # find first avail column name for period
    period = get_first_available_value(
        row,
        ['period_minutes', 'Period (minutes)', 'Period (Minutes)', 'PERIOD_MINUTES', 'PERIOD']
    )

    # if period is already available, return it directly without any calculations
    if pd.notna(period):
        return period
    
    # find first avail column name for perigee
    perigee = get_first_available_value(
        row,
        ['perigee_km', 'Perigee (km)', 'Perigee (KM)', 'PERIGEE_KM', 'PERIGEE']
    )
    
    # find first avail column name for apogee
    apogee = get_first_available_value(
        row,
        ['apogee_km', 'Apogee (km)', 'Apogee (KM)', 'APOGEE_KM', 'APOGEE']
    )

    # if either perigee or apogee are missing, we cannot calculate the period, return nan.
    if pd.isna(perigee) or pd.isna(apogee):
        return np.nan

    # Kepler's Third Law: T = 2 * pi * sqrt(a^3 / mu), where T is the orbital period in seconds,
    # a is the semi-major axis in kilometers, and mu is Earth's gravitational parameter.
    alt_km = (perigee + apogee) / 2
    a = earth_radius + alt_km
    period_seconds = 2 * np.pi * np.sqrt(a**3 / mu)

    # Convert the period from seconds to minutes before returning.
    return period_seconds / 60

def get_first_available_value(row, column_names):
    """
    Return the first available value from a row for any of the provided column names.
    This allows us to support multiple potential column name variations for the same underlying data,
    which is common in our dataset. The function checks for the presence of each candidate column name
    in the row and returns the value from the first one that exists. If none of the candidate columns are
    present, it returns np.nan.

    Parameters:
    row (pd.Series): A row from a DataFrame.
    column_names (list[str] | tuple[str, ...]): Candidate column names in priority order.

    Returns:
    object: The value from the first matching column, or np.nan if none are present.
    """
    for column_name in column_names:
        if column_name in row.index:
            return row[column_name]
    return np.nan

#########################################################################################################
# AI Assisted Function: derive_eccentricity                                                             #
#                                                                                                       #
# What this does                                                                                        #
# - Calculates orbital eccentricity from perigee and apogee altitudes.                                  #
# - Uses the formula: e = (ra - rp) / (ra + rp), where ra and rp are distances from Earth's center.     #
# - Accounts for Earth's radius to convert altitudes to distances from Earth's center.                  #
#                                                                                                       #
# How AI assistance was used                                                                            #
# - I understand the concept of eccentricity but wasn't sure of the formula to use                      #
#   (the function itself is straightforward once the formula is known). AI provided the formula for     #
#   eccentricity, I provided the implementation.                                                        #
#                                                                                                       #
# AI (GitHub Copilot, Various Models) assisted with formula reconstruction.                              #
#########################################################################################################
def derive_eccentricity(row):
    ra = row['apogee_km'] + earth_radius  # Distance from Earth center to apogee
    rp = row['perigee_km'] + earth_radius  # Distance from Earth center to perigee
    return (ra - rp) / (ra + rp)

#########################################################################################################
# AI Assisted Function: fit_growth_regimes                                                              #
#                                                                                                       #
# What this does                                                                                        #
# - Splits the yearly series into pre/post regimes using a candidate split year.                        #
# - Fits a linear trend to the legacy regime (pre-split).                                               #
# - Fits an exponential trend to the modern regime (post-split) using a log-space linear fit.           #
# - Uses year-centering and exponent clipping for numerical stability in exponential reconstruction.    #
# - Returns fitted segments and key metrics (legacy slope, exponential growth rate, doubling time).     #
#                                                                                                       #
# How AI assistance was used                                                                            #
# - I defined the analysis method (legacy linear vs modern exponential) and fit requirements.           #
# - AI helped draft a clean reusable function structure and stability safeguards.                       #
#                                                                                                       #
# AI (GitHub Copilot, Various Models) assisted with formula and function implementation.                 #
#########################################################################################################
def fit_growth_regimes(df, split_year, y_col):
    """
    Fit linear and exponential growth regimes to the data split by a candidate year.
    
    Parameters:
    df (pd.DataFrame): The input DataFrame containing 'launch_year' and the target y_col.
    split_year (int): The candidate year to split the data into legacy and modern regimes.
    y_col (str): The name of the column in df that contains the values to fit.
    
    Returns:
    pre (pd.DataFrame): The subset of df for the legacy regime with an added 'trend_linear' column.
    post (pd.DataFrame): The subset of df for the modern regime with an added 'trend_exponential' column.
    m_pre (float): The slope of the linear fit for the legacy regime.
    b_exp (float): The exponential growth rate for the modern regime.
    doubling_time (float): The doubling time for the modern regime based on the exponential fit.
    """
    pre = df[df['launch_year'] <= split_year].copy()
    post = df[df['launch_year'] > split_year].copy()

    if len(pre) < 3 or len(post) < 3:
        raise ValueError('Not enough data points on both sides of split year.')

    # Legacy regime: linear fit y = m_pre * year + b_pre
    m_pre, b_pre = np.polyfit(pre['launch_year'], pre[y_col], 1)
    pre['trend_linear'] = m_pre * pre['launch_year'] + b_pre

    # Modern regime: exponential fit y = a0 * exp(b_exp * (year - year0))
    # Centering the year axis keeps exponent values numerically stable.
    post_fit = post[post[y_col] > 0].copy()
    if len(post_fit) < 3:
        raise ValueError('Not enough positive post-split values for exponential fit.')

    year0 = float(post_fit['launch_year'].min())
    x_post = post_fit['launch_year'] - year0
    b_exp, log_a0 = np.polyfit(x_post, np.log(post_fit[y_col]), 1)
    a0 = np.exp(log_a0)

    x_all_post = post['launch_year'] - year0
    exp_term = np.exp(np.clip(b_exp * x_all_post, -700, 700))
    post['trend_exponential'] = a0 * exp_term

    # Doubling time from exponential rate: ln(2)/b
    doubling_time = np.inf if b_exp <= 0 else (np.log(2) / b_exp)
    return pre, post, m_pre, b_exp, doubling_time


#########################################################################################################
# AI Assisted Function: choose_split_year                                                               #
#                                                                                                       #
# Definitions:                                                                                          #
# SSE: Sum of Squared Errors, a measure of the total deviation of predicted values from observed values.#                                                                                 
# RMSE: Root Mean Squared Error, a measure of the differences between predicted and observed values.    #
# 
# What this does                                                                                        #
# - Builds candidate split years from observed launch years.                                            #
# - Applies minimum sample-size constraints for pre/post regimes.                                       #
# - Calls fit_growth_regimes for each valid candidate split year.                                       #
# - Computes SSE/RMSE for each candidate and ranks model fit quality.                                   #
# - Returns the best split year (lowest RMSE) plus a diagnostics table for transparency.                #
# - Skips candidates that fail fitting (insufficient/invalid post-split behavior).                      #
#                                                                                                       #
# How AI assistance was used                                                                            #
# - I defined the objective (data-selected decoupling year, not a pre-asserted date).                   #
# - AI helped structure the candidate-evaluation loop and diagnostics output.                           #
#                                                                                                       #
# AI (GitHub Copilot, Various Models) assisted with formula and function design/implementation.          #
#########################################################################################################
def choose_split_year(df, y_col, min_pre_points=8, min_post_points=6):
    """
    Choose the optimal split year for separating legacy and modern growth regimes.

    Parameters:
    df (pd.DataFrame): The input DataFrame containing 'launch_year' and the target y_col.
    y_col (str): The name of the column in df that contains the values to fit.
    min_pre_points (int): Minimum number of data points required in the pre-split regime. 
    min_post_points (int): Minimum number of data points required in the post-split regime.

    Returns:
    best_split_year (int): The year that provides the best split based on RMSE.   
    split_diagnostics (pd.DataFrame): A DataFrame containing diagnostics for each candidate split year.   
    """
    years = sorted(df['launch_year'].dropna().astype(int).unique())
    results = []

    for split_year in years:
        pre_n = (df['launch_year'] <= split_year).sum()
        post_n = (df['launch_year'] > split_year).sum()
        if pre_n < min_pre_points or post_n < min_post_points:
            continue

        try:
            pre, post, _, _, _ = fit_growth_regimes(df, split_year=split_year, y_col=y_col)
            pre_sse = ((pre[y_col] - pre['trend_linear']) ** 2).sum()
            post_sse = ((post[y_col] - post['trend_exponential']) ** 2).sum()
            total_sse = pre_sse + post_sse
            total_n = len(pre) + len(post)
            rmse = np.sqrt(total_sse / max(total_n, 1))

            results.append({
                'split_year': split_year,
                'pre_n': int(pre_n),
                'post_n': int(post_n),
                'rmse': float(rmse),
                'total_sse': float(total_sse)
            })
        except Exception:
            continue

    if not results:
        raise ValueError('No valid candidate split year found with current constraints.')

    split_diagnostics = pd.DataFrame(results).sort_values('rmse').reset_index(drop=True)
    best_split_year = int(split_diagnostics.loc[0, 'split_year'])
    return best_split_year, split_diagnostics