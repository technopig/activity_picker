# Overview
The objective is to create a `Flask` application that can serve up a simple suggestion: what activity should I do tomorrow?

## How it will work
1. Define all desired activities
1. Define all relevant conditions (such as recent precip, future temps, etc)
1. Define perfect conditions for each activity
1. Create a weighted scoring system according to how important each condition is
1. Find data sources for each condition
1. Pull and process data to assign each activity a score
1. *DISPLAY HIGHEST SCORING ACTIVITY*

## Setup
Execute
```
DD_VERSION="1.5" DD_SERVICE="activity_picker" DD_ENV="macbookpro" DD_LOGS_INJECTION=true DD_TRACE_SAMPLE_RATE="1" DD_PROFILING_ENABLED=true ddtrace-run flask run --port 5016
```

# Activities
- Mountain Biking
- Hiking
- Backcountry Skiing
- Inbounds Skiing
- Mountaineering
- River Tubing
- Rock Climbing
- Stay inside

# Relevant Conditions
- Temperature - forecast
- Temperature - recent past
- cloud cover - forecast
- precipitation - forecast
- precipitation - recent past
- water flow rate in river - recent past
- avalanche - forecast

# Perfect Conditions and Scoring System (max of 5)
### Mountain Biking
- [3] Temp: 65 degrees
- [3] Sunny
- [5] hasn't rained in 3 days
- [4] No precip

### Hiking
- [3] Temp: 55 degrees
- [2] Mostly Sunny
- [4] hasn't rained in 2 days
- [4] No precip

### Backcountry Skiing
- [5] low avy risk
- [3] recent snow (smooth surface)
  - [3] not too much - maybe 5" or so
- [4] styrofoam snow to walk on
- [3] Temp: 31 degrees
- [2] very light snow
- [4] low overnight temperatures (<20 degrees)

### Inbounds Skiing
- [4] powder on the ground
  - the bigger the precip/SWE the better
- [2] not icy
  - [need to define this]
- [4] 30 degrees and overcast OR
- [4] 10 degrees and sunny
- [1] not snowing
- [3] low overnight temperatures (<20 degrees)

### Mountaineering
- [4] low overnight temperatures (<30 degrees)
- [2] temp: 45 degrees at 10 AM
- [3] overcast or partly Sunny (to keep snow hard)
- [5] zero avy risk (consolidated spring snow)
- [3] no precip
- [3] recent lower temps


### River Tubing
- [4] Temp: 95 degrees
- [4] Water flow: 200 CFS
- [4] Sunny


### Rock Climbing
- [3] Temp: 70 degrees
- [3] Sunny
- [99] high stoke
- [2] hasn't rained in 2 days
- [4] no precip


### Stay inside and drink hot cocoa
- [5] VERY cold (temps less than 10 below)
- [5] Heavy precipitation all day
- [5] storm conditions

# Data Sources
- Snow (snotel sites; weather stations; forecasts)
- Wind (weather stations; forecasts)
- Rain (weather stations; forecasts)
- Temperature (weather stations; forecasts)
- Water Flow (water gauges)
- Water Temperature (water gauges)

# Future Ideas
- allow the user to define optimal conditions
- allow the user to define activities
- test scoring system with real data to confirm fairness/accuracy
