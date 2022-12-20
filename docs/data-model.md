# Data models

## Watchlists DB (Postgres)

### Movie

A `Movie` model instance contains detailed data about a given film.

| Name | Type | Unique | Optional |
|-|-|-|-|
| id | SERIAL | yes | no |
| tmdb_id | INT | yes | no |
| title | VARCHAR | no | no |
| poster_path | VARCHAR | no | yes |
| runtime | INT | no | yes |
| genres | M2M join table with `Genre` | no | yes |

### Genre

A `Genre` model instance contains a genre that one or many Movies are a part of.

| Name | Type | Unique | Optional |
|-|-|-|-|
| id | SERIAL | yes | no |
| tmdb_id | INT | yes | no |
| name | VARCHAR | yes | no |

### Review

| Name | Type | Unique | Optional |
|-|-|-|-|
| id | SERIAL | yes | no |
| user | INT REFERENCES `UserVO`(id) | no | no |
| movie | INT REFERENCES `Movie`(id) | no | no |
| title | VARCHAR | no | no |
| content | VARCHAR | no | no |
| date_created | DATE | no | no |
| date_updated | DATE | no | no |

### Rating

| Name | Type | Unique | Optional |
|-|-|-|-|
| id | SERIAL | yes | no |
| user | INT REFERENCES `UserVO`(id) | no | no |
| movie | INT REFERENCES `Movie`(id) | no | no |
| score | INT | no | no |
| date | DATE | no | no |

### Watchlist Table
Consider making a watchlist ownable by multiple people

| Name | Type | Unique | Optional |
|-|-|-|-|
| id | SERIAL | yes | no |
| owners | M2M join table with `UserVO`(id) | no | no |
| name | VARCHAR | no | no |
| description | VARCHAR | no | yes |
| date_created | DATE | no | no |
| date_updated | DATE | no | no |

### WatchlistItem Table

| Name | Type | Unique | Optional |
|-|-|-|-|
| id | SERIAL | yes | no |
| movie | INT REFERENCES `Movie`(id) | no | no |
| interest_level | INT (1 to 3) | no | no |
| watchlist | INT REFERENCES `Watchlist`(id) | no | no |
| date_added | DATE | no | no |
| watched | BOOLEAN | no | no |
| interest | INT | no | no |

### UserVO Table

| Name | Type | Unique | Optional |
|-|-|-|-|
| id | SERIAL | yes | no |
| username | VARCHAR | no | no |
| email | VARCHAR | no | yes |

## Watch Party DB (Postgres)

### Watchparty Table

| Name | Type | Unique | Optional |
|-|-|-|-|
| id | SERIAL | yes | no |
| host | INT REFERENCES `UserVO`(id) | no | no |
| name | VARCHAR | no | no |
| description | VARCHAR | no | yes |
| genres | M2M join table with `Genre`(id) | no | yes |
| date | DATE | no | yes |

### WatchpartyAttendee Table

| Name | Type | Unique | Optional |
|-|-|-|-|
| id | SERIAL | yes | no |
| user | INT REFERENCES `UserVO`(id) | no | no |
| watchparty | INT REFERENCES `Watchparty`(id) | no | no |

### UserVO Table

| Name | Type | Unique | Optional |
|-|-|-|-|
| id | SERIAL | yes | no |
| username | VARCHAR | no | no |
| email | VARCHAR | no | yes |

## Accounts DB (Postgres)

### User Table

| Name | Type | Unique | Optional |
|-|-|-|-|
| id | SERIAL | yes | no |
| username | VARCHAR | no | no |
| email | VARCHAR | no | yes |
| password | VARCHAR | no | no |
