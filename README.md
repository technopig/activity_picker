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

# Activities
- Mountain Biking
- Hiking
- Backcountry Skiing
- Inbounds Skiing
- Mountaineering
- River Tubing
- Rock Climbing
- Stay inside

# Perfect Conditions
### Mountain Biking
- Temp: 65 degrees
- Sunny
- hasn't rained in 3 days
- No precip

### Hiking
- Temp: 55 degrees
- Mostly Sunny
- hasn't rained in 2 days
- No precip

### Backcountry Skiing
- low avy risk
- recent snow (smooth surface)
  - not too much - maybe 5" or so
- styrofoam snow to walk on
- Temp: 31 degrees
- very light snow
- low overnight temperatures (<20 degrees)

### Inbounds Skiing
- powder on the ground
  - the bigger the precip/SWE the better
- not icy
  - [need to define this]
- 30 degrees and overcast OR
- 10 degrees and sunny
- not snowing
- low overnight temperatures (<20 degrees)

### Mountaineering
- low overnight temperatures (<30 degrees)
- temp: 45 degrees at 10 AM
- overcast or partly Sunny (to keep snow hard)
- zero avy risk (consolidated spring snow)
- no precip
- recent lower temps


### River Tubing
- Temp: 95 degrees
- Water flow: 200 CFS
- Sunny


### Rock Climbing
- Temp: 70 degrees
- Sunny
- high stoke
- hasn't rained in 2 days
- no precip


### Stay inside and drink hot cocoa
- VERY cold (temps less than 10 below)
- Heavy precipitation all day
- storm conditions

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
