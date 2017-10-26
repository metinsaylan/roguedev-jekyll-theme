---
layout: page
title: Countdown Widget Help
desc: Descriptions for the options and widget inputs
redirect_from: /projects/wordpress/countdown-widget/help/
permalink: /docs/countdown-widget-help/
---

This page is about [Countdown Widget (Free)](/projects/wordpress/countdown-widget/) for WordPress.

<h3 id="title">Title</h3>

<p>This is title for the widget. You can leave it blank or give your widget a title like "Final Countdown"</p>

***

<h3 id="event-title">Event Title</h3>

<p>This text will be displayed at the bottom of countdown. You can leave it blank or you can enter a phrase about the event like “until my birthday!”. This will explain why you are counting down. </p>

> **Note** you can use html in this field to add links.

***

<h3 id="date">Date</h3>

<p>This is the date we are counting down to. If you enter a past date countdown won’t work.</p>

***

<h3 id="time">Time</h3>

Hours, Minutes and seconds of countdown. Any problems with that?

***

<h3 id="format">Format</h3>
<p>This is where you can change how your countdown is displayed. Here are basic elements you can use in this field:</p>

<pre>Y : years
O : months
W : weeks
D : days
H : hours
M : minutes
S : seconds
</pre>

The basic countdown format is <code>HMS</code> which will display, hours, minutes and seconds.

Using lower case letters will hide "0" (zero) values from the countdown. For example if you use `yowdHMS` as format then it will hide year, month, week and day values once they are "0". If you want to show days only you can use ``D`` as format text.

***

<h3 id="color">Color</h3>

This is the text color of countdown widget. You can use three letter hexadecimal colors as well as 6-digit colors. See a <a href="{{ site.imgbase }}/html-color-codes.png">list of html colors you can use here</a>.

***

<h3 id="background-color">Background color</h3>

This is background color of countdown area. You can leave it blank to leave it transparent. Default gray background is : `#ddd`

***

<h3 id="width">Width</h3>

This is the width of the countdown layer. Countdown auto size contents to fit this width. If none is entered it will expand to full width of sidebar.
