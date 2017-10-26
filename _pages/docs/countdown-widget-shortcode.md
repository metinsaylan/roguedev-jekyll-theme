---
layout: page
title: Countdown Widget Shortcode Documentation
desc: Easy way to add countdown timers to your WordPress posts
permalink: /docs/countdown-widget-shortcode/
---
[Countdown Widget](http://metinsaylan.com/projects/wordpress/countdown-widget/) shortcode usage is the easiest way to add countdown timers to your WordPress posts. Basic shortcode usage:

```
[countdown date="01 January 2018" link="false"]
```

```
[countup date="01 April 1980" link="false"]
```

### Event title

If you want to display an event title under your countdown widget you can add `event="Sample Title"` to your countdown shortcode as given below:

```
[countdown event="Testing shortcode" date="12 June"]
```

### Adding hours and minutes

If no time is added countdown uses midnight as base. If you want to countdown to or count up from a specific time you can add hour and minutes to your shortcode as you can see in the sample below:

```
[countdown date="12 June" hour="18" minutes="54"]
```

### All possible attributes

* `title="Widget Title"` : Adds widget title before countdown widget
* `event="Event Title"` : Event title that we are counting down
* `date="12 June"` : This is a shorthand function for month, day and year. It depends on PHP strtotime function so it doesn't work with every human readible format. Basic date format should be like `12 June 2020`.
* `direction="down"` : You can count down or up using this option.
* `timezone="+2"` : Timezone of the countdown. This is required if you are creating a global countdown!

* `month="10"` : Month of the countdown date
* `day="12"` : Day of the countdown date
* `year="2020"` : Year of the countdown date

* `hour="12"` : Hour part of the countdown time
* `minutes="00"` : Minutes part of the countdown time
* `seconds="00"` : Seconds part of the countdown time

* `format="yowdHMS"` : A key to hide/show certain digits on countdown. Check [explanation here](http://metinsaylan.com/docs/countdown-widget-help/#format).

* `color="#900"` : Text color of the countdown
* `bgcolor="#000"` : Background color of the widget
* `width="200"` : Width of the widget in pixels
* `height="200"` : Height of the widget in pixels
* `radius="8"` : Border radius of the widget in pixels
* `link="false"` : Hides support link from the widget
