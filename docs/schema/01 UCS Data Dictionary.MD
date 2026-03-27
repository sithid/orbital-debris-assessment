
# Cleaned UCS Registry: Data Dictionary

**Purpose:** Define the schema for the cleaned UCS Satellite Registry, used for satellite-focused analysis and integration with other orbital datasets.

## 1. Identity & Classification

| Feature Name      | Type     | Description                                                                 |
| :---------------- | :------- | :-------------------------------------------------------------------------- |
| `norad_id`        | `int`    | Unique USSPACECOM catalog number. Primary join key for SATCAT.              |
| `cospar_id`       | `str`    | International launch designator.                                            |
| `primary_purpose` | `str`    | Simplified mission category for analysis.                                   |
| `un_registry`     | `str`    | Country or organization of UN registration.                                 |
| `country_operator`| `str`    | Main operator country.                                                      |

## 2. Physical & Operational Profile

| Feature Name      | Type     | Description                                                                 |
| :---------------- | :------- | :-------------------------------------------------------------------------- |
| `launch_mass_kg`  | `float`  | Total mass at launch. Filled using grouped medians and safety checks.       |
| `dry_mass_kg`     | `float`  | Estimated dry mass (no fuel), based on orbit-specific ratios.               |
| `power_watts`     | `float`  | Power output in watts, standardized and filled as needed.                   |
| `lifetime_years`  | `float`  | Expected service life, filled from orbit-level medians.                     |
| `sat_age_years`   | `int`    | Satellite age in 2026 ($2026 - launch\_year$).                              |

## 3. Orbital State & Geometry

| Feature Name         | Type     | Description                                                                |
| :------------------- | :------- | :------------------------------------------------------------------------- |
| `period_minutes`     | `float`  | Time for one orbit. Rebuilt with Kepler logic when geometry available.     |
| `perigee_km`         | `float`  | Closest point to Earth.                                                    |
| `apogee_km`          | `float`  | Farthest point from Earth.                                                 |
| `inclination_degrees`| `float`  | Orbit angle relative to Earth’s equator.                                   |
| `eccentricity`       | `float`  | How circular or stretched the orbit is (non-negative).                     |
| `orbit_class`        | `str`    | Standardized regime: `LEO`, `MEO`, `GEO`, `Elliptical`.                    |
| `orbit_type`         | `str`    | Standardized geometry: `Polar`, `Equatorial`, `Inclined`, `Eccentric`.     |
| `geo_longitude`      | `float`  | GEO position if relevant (0.0 for non-GEO payloads).                       |

## 4. Dates & Status Flags

| Feature Name      | Type      | Description                                                                 |
| :---------------- | :-------  | :-------------------------------------------------------------------------- |
| `launch_date`     | `datetime`| Standardized launch date.                                                   |
| `launch_year`     | `int`     | Year extracted from launch date.                                            |
| `is_commercial`   | `int`     | 1 if commercial use is present; else 0.                                     |
| `is_military`     | `int`     | 1 if military use is present; else 0.                                       |
| `is_government`   | `int`     | 1 if government use is present; else 0.                                     |
| `is_civil`        | `int`     | 1 if civil use is present; else 0.                                          |
