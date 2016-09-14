# Angle Between Clock Hands (https://www.codewars.com/kata/543ddf69386034670d000c7d)

Given a Date, return the angle between the two hands of a 12-hour analog clock in radians.

For example, at 3:00 the angle is π/2 (90 degrees).

Return the smaller of the angles ( <= π ).

Return π if the hands are opposite.

Note: The hour hand does not "snap" to the tick mark - e.g. at 6:30 the angle is not 0 because the hour hand is at 6.5, not 6.0.

There is no "seconds" hand, so the minutes hand snaps to the minute.