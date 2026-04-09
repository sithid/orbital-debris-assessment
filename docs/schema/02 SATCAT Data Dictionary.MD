
# Cleaned SATCAT Registry: Data Dictionary

**Purpose:** Defines the schema for the cleaned SATCAT registry, used for debris, rocket body, and payload tracking, and for integration with UCS and other orbital datasets.

---

## 1. Physical & Kinetic Properties

| Feature Name      | Type     | Description                                                                 |
| :---------------- | :------- | :-------------------------------------------------------------------------- |
| `launch_mass_kg`  | `float`  | High-fidelity mass from UCS registry. `NaN` for debris.                     |
| `proxy_mass_kg`   | `float`  | Final kinetic mass (UCS or ESA proxies).                                    |
| `dry_mass_kg`     | `float`  | Structural mass, derived using orbit-specific dry-to-wet ratios.            |
| `rcs`             | `float`  | Radar cross section ($m^2$), sanitized and filled via categorical baselines.|
| `rcs_class`       | `str`    | Size bin: `SMALL`, `MEDIUM`, `LARGE` (from RCS).                            |
| `sat_age_years`   | `int`    | Calculated age ($2026 - launch_year$) for fragmentation modeling.           |

---

## 2. Orbital Mechanics

| Feature Name         | Type     | Description                                                                |
| :------------------- | :------- | :------------------------------------------------------------------------- |
| `period_minutes`     | `float`  | Time for one orbit (Kepler's 3rd Law: $T = 2\pi\sqrt{a^3/\mu}$).           |
| `inclination_degrees`| `float`  | Angle relative to equator (for collision probability maps).                |
| `apogee_km`          | `float`  | Highest altitude point in orbit.                                           |
| `perigee_km`         | `float`  | Lowest altitude point in orbit.                                            |
| `eccentricity`       | `float`  | Deviation from circularity, derived from altitudes.                        |
| `orbit_class`        | `str`    | Standardized regime: `LEO`, `MEO`, `GEO`, `Elliptical`.                    |

---

## 3. Categorical & Temporal Metadata

| Feature Name      | Type     | Description                                                                 |
| :---------------- | :------- | :-------------------------------------------------------------------------- |
| `norad_id`        | `int`    | Primary merge key, normalized for 1:1 join-readiness.                       |
| `cospar_id`       | `str`    | International designator (COSPAR ID), scrubbed and capitalized.             |
| `object_type`     | `str`    | Controlled vocabulary: `PAYLOAD`, `ROCKET BODY`, `DEBRIS`, `UNKNOWN`.       |
| `ops_status`      | `str`    | Health status: `OPERATIONAL`, `NON-OPERATIONAL`, etc.                       |
| `owner_code`      | `str`    | ISO-style country/org code, whitespace stripped.                            |
| `launch_year`     | `int`    | Year of launch, derived for simulation aging.                               |
| `in_orbit`        | `int`    | 1 if currently in orbit, 0 if decayed.                                      |

## 4. Acronyms & Definitions

| Acronym | Definition                           |
| :------ | :----------------------------------- |
| `UCS`   | Union of Concerned Scientists        |
| `ESA`   | European Space Agency                |
| `RCS`   | Radar Cross Section                  |
| `LEO`   | Low Earth Orbit (altitude < 2000 km) |
| `MEO`   | Medium Earth Orbit (2000-35786 km)   |
| `GEO`   | Geostationary Orbit (35786 km)       |
| `Elliptical` | Highly eccentric orbit (varied altitudes) |
| `PAYLOAD` | Operational satellite or spacecraft |
| `ROCKET BODY` | Spent rocket stage or booster |
| `DEBRIS` | Fragmented object or non-functional piece |
| `UNKNOWN` | Unclassified object type |
| `OPERATIONAL` | Actively functioning satellite |
| `NON-OPERATIONAL` | No longer functioning, but still in orbit |
