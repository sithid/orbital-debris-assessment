# Orbital Debris Database: Data Dictionary

**Purpose:** Defines the schema for the synthesized orbital_debris.db SQL database, the analytical backbone for all orbital debris queries and risk modeling.

---

## 1. satellites

| Feature Name      | Type     | Description                                      |
| :---------------- | :------- | :----------------------------------------------- |
| `norad_id`        | `int`    | Unique USSPACECOM catalog number (primary key).  |
| `cospar_id`       | `str`    | International launch designator.                 |
| `object_name`     | `str`    | Universal object label.                          |
| `satellite_name`  | `str`    | Common/commercial satellite name.                |
| `official_name`   | `str`    | Official registry name.                          |
| `object_type`     | `str`    | Source class: PAYLOAD, ROCKET BODY, DEBRIS.      |
| `category`        | `str`    | Engineered risk class.                           |
| `ops_status`      | `str`    | Operational status.                              |
| `data_status`     | `str`    | Tracking health/status.                          |
| `in_orbit`        | `int`    | 1 if in orbit, 0 if decayed.                     |
| `owner_code`      | `str`    | Standardized operator code.                      |
| `launch_id`       | `str`    | Synthetic launch event ID (YYYY-NNN).            |

---

## 2. orbital_data

| Feature Name         | Type     | Description                                    |
| :------------------- | :------- | :--------------------------------------------- |
| `norad_id`           | `int`    | Foreign key to satellites.                     |
| `orbit_class`        | `str`    | Regime: LEO, MEO, GEO, etc.                    |
| `orbit_type`         | `str`    | Geometry: Polar, Sun-Synchronous, etc.         |
| `period_minutes`     | `float`  | Orbital period (minutes).                      |
| `perigee_km`         | `float`  | Closest approach to Earth (km).                |
| `apogee_km`          | `float`  | Farthest distance from Earth (km).             |
| `inclination_degrees`| `float`  | Orbit inclination (degrees).                   |
| `eccentricity`       | `float`  | Orbit shape (0 = circular).                    |
| `semi_major_axis_km` | `float`  | Semi-major axis (km).                          |
| `launch_mass_kg`     | `float`  | Mass at launch (kg).                           |
| `proxy_mass_kg`      | `float`  | Modeled/estimated mass (kg).                   |
| `dry_mass_kg`        | `float`  | Structural mass, no fuel (kg).                 |
| `power_watts`        | `float`  | Power generation (watts).                      |
| `proxy_power_watts`  | `float`  | Imputed power (watts).                         |
| `rcs`                | `float`  | Radar cross section (m²).                      |
| `rcs_class`          | `str`    | Size class: SMALL, MEDIUM, LARGE.              |

---

## 3. ucs_details

| Feature Name      | Type     | Description                                    |
| :---------------- | :------- | :--------------------------------------------- |
| `norad_id`        | `int`    | Foreign key to satellites.                     |
| `lifetime_years`  | `float`  | Design life expectancy (years).                |
| `sat_age_years`   | `int`    | Object age in years.                           |
| `primary_purpose` | `str`    | Main mission type.                             |
| `detailed_purpose`| `str`    | Granular mission detail.                       |
| `geo_longitude`   | `float`  | GEO longitude (if applicable).                 |
| `un_registry`     | `str`    | UN registration status.                        |

---

## 4. risk_assessment

| Feature Name    | Type     | Description                                    |
| :-------------- | :------- | :--------------------------------------------- |
| `norad_id`      | `int`    | Foreign key to satellites.                     |
| `velocity_kms`  | `float`  | Mean orbital velocity (km/s).                  |
| `kinetic_joules`| `float`  | Kinetic energy (Joules).                       |
| `is_zombie`     | `int`    | 1 if payload exceeds design life + 10%.        |

---

## 5. ownership_operators

| Feature Name        | Type     | Description                                 |
| :------------------ | :------- | :------------------------------------------ |
| `owner_code`        | `str`    | Operator code (primary key).                |
| `owner`             | `str`    | Canonical owner name.                       |
| `country_operator`  | `str`    | Country of operator.                        |
| `users`             | `str`    | User sector(s): Commercial, Military, etc.  |
| `is_commercial`     | `int`    | 1 if commercial, else 0.                    |
| `is_government`     | `int`    | 1 if government, else 0.                    |
| `is_military`       | `int`    | 1 if military, else 0.                      |
| `is_civil`          | `int`    | 1 if civil, else 0.                         |
| `contractor`        | `str`    | Prime manufacturer.                         |
| `contractor_country`| `str`    | Manufacturer country.                       |

---

## 6. launch_events

| Feature Name    | Type     | Description                                    |
| :-------------- | :------- | :--------------------------------------------- |
| `launch_id`     | `str`    | Synthetic launch event ID (primary key).       |
| `launch_date`   | `str`    | Date of launch (ISO format).                   |
| `launch_year`   | `int`    | Year of launch.                                |
| `launch_site`   | `str`    | Launch site/location.                          |

---
