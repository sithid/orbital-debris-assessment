
# Synthesized Kinetic Master Registry: Data Dictionary

**Purpose:** Defines the schema for the Kinetic Master dataset, the cleaned and merged result of UCS and SATCAT, used for orbital debris SQL modeling and analysis.

**Scope Legend:**

- **Global:** Mandatory for all objects (Debris, Rocket Bodies, Payloads)
- **Payload:** Only for satellites (assets)

---

## 1. Identity & Classification

| Feature Name      | Type     | Scope     | Description                                                           |
| :---------------- | :------- | :-------- | :-------------------------------------------------------------------- |
| `norad_id`        | `str`    | Global    | Unique USSPACECOM catalog number (primary key).                       |
| `cospar_id`       | `str`    | Global    | International Designator (Launch Year + Launch Number).               |
| `object_name`     | `str`    | Global    | Universal label (UCS name for Payloads; SATCAT for Debris).           |
| `satellite_name`  | `str`    | Payload   | Commercial/common name (Payloads only).                               |
| `official_name`   | `str`    | Payload   | Official registry name (Payloads only).                               |
| `category`        | `str`    | Global    | Engineered risk class: `Active`, `Inactive`, `Rocket Body`, `Debris`. |
| `object_type`     | `str`    | Global    | Raw source class: `PAYLOAD`, `ROCKET BODY`, `DEBRIS`.                 |

---

## 2. Kinetic Profile (Physics)

| Feature Name        | Type     | Scope     | Description                                                        |
| :------------------ | :------- | :-------- | :----------------------------------------------------------------- |
| `launch_mass_kg`    | `float`  | Payload   | Mass at launch (raw data).                                         |
| `proxy_mass_kg`     | `float`  | Global    | Mass model (high-fidelity UCS or ESA proxies).                     |
| `dry_mass_kg`       | `float`  | Global    | Structural mass (no fuel), via fuel-fraction constants.            |
| `velocity_kms`      | `float`  | Global    | Mean velocity (Vis-Viva: $v=\sqrt{\mu/a}$).                        |
| `kinetic_joules`    | `float`  | Global    | Impact energy ($E_k = \frac{1}{2}mv^2$).                           |
| `power_watts`       | `float`  | Payload   | Electrical power generation (raw data).                            |
| `proxy_power_watts` | `float`  | Payload*  | Imputed power (Watts). *0 for Debris.*                             |
| `rcs`               | `float`  | Global    | Radar cross section ($m^2$).                                       |
| `rcs_class`         | `str`    | Global    | Size category: `LARGE`, `MEDIUM`, `SMALL`.                         |

---

## 3. Orbital State & Geometry

| Feature Name         | Type     | Scope     | Description                                                        |
| :------------------- | :------- | :-------- | :----------------------------------------------------------------- |
| `orbit_class`        | `str`    | Global    | Standardized regime: `LEO`, `MEO`, `GEO`.                          |
| `orbit_type`         | `str`    | Payload   | Geometric class (e.g., `Polar`, `Sun-Synchronous`).                |
| `perigee_km`         | `float`  | Global    | Closest approach to Earth.                                         |
| `apogee_km`          | `float`  | Global    | Farthest distance from Earth.                                      |
| `semi_major_axis_km` | `float`  | Global    | Orbit "radius" (base for velocity calc).                           |
| `inclination_degrees`| `float`  | Global    | Angle relative to equator.                                         |
| `eccentricity`       | `float`  | Global    | Orbit shape (0 = circular).                                        |
| `period_minutes`     | `float`  | Global    | Time to complete one orbit.                                        |

---

## 4. Mission Intelligence

| Feature Name      | Type     | Scope     | Description                                                        |
| :---------------- | :------- | :-------- | :----------------------------------------------------------------- |
| `primary_purpose` | `str`    | Payload   | Mission type (e.g., `Communications`, `Earth Observation`).        |
| `detailed_purpose`| `str`    | Payload   | Granular mission detail.                                           |
| `users`           | `str`    | Payload   | Consolidated user string (e.g., "Commercial/Military").            |
| `country_operator`| `str`    | Payload   | Nation operating the payload.                                      |
| `is_commercial`   | `int`    | Payload   | 1 if commercial utility; else 0.                                   |
| `is_government`   | `int`    | Payload   | 1 if government utility; else 0.                                   |
| `is_military`     | `int`    | Payload   | 1 if military utility; else 0.                                     |
| `is_civil`        | `int`    | Payload   | 1 if civil utility; else 0.                                        |

---

## 5. Lifecycle & Status

| Feature Name      | Type     | Scope     | Description                                                        |
| :---------------- | :------- | :-------- | :----------------------------------------------------------------- |
| `launch_date`     | `date`   | Global    | Date of orbital insertion.                                         |
| `launch_year`     | `int`    | Global    | Year of launch.                                                    |
| `sat_age_years`   | `int`    | Global    | Object age ($2026 - launch\_year$).                                |
| `lifetime_years`  | `float`  | Payload   | Design life expectancy.                                            |
| `ops_status`      | `str`    | Global    | Operational status: `OPERATIONAL`, `DECAYED`, etc.                 |
| `data_status`     | `str`    | Global    | Tracking health: `Lost` = Issue; `NaN` = Healthy.                  |
| `in_orbit`        | `int`    | Global    | 1 if currently in orbit; else 0.                                   |
| `is_zombie`       | `int`    | Payload   | 1 if Payload Age > Design Life + 10%.                              |

---

## 6. Supply Chain & Metadata

| Feature Name        | Type     | Scope     | Description                                                        |
| :------------------ | :------- | :-------- | :----------------------------------------------------------------- |
| `owner`             | `str`    | Global    | Standardized operator code (e.g., `US`, `PRC`).                    |
| `owner_code`        | `str`    | Global    | Raw source code from SATCAT.                                       |
| `contractor`        | `str`    | Payload   | Prime manufacturer of bus/payload.                                 |
| `contractor_country`| `str`    | Payload   | Nation of manufacture.                                             |
| `contractor_country` | `str` | Payload | Nation of manufacture. |
