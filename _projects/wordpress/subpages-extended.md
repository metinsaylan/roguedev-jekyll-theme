---
layout: page
title: Subpages Extended
subtitle: Subpages Extended
desc: List sub pages of a page easily, using shortcode and widget.
redirect_from: /wordpress/plugins/subpages-widget/
---
Subpages Extended plugin for WordPress, enables you to list sub pages of a post easily using both shortcode and widget functionality.

### Description

This widget displays subpages of a page easily. Though it's main power is the `[subpages]` shortcode. Using this shortcode on a page you can create subpage indexes. You can view live demo on my <a href="http://shailan.com/wordpress">wordpress</a> page. It automatically generates subpage indexes. You can also list subpages of another page using the <strong>childof</strong> attribute of shortcode. See the examples below:

***

Here are subpages of my wordpress page with a depth level of 1:

`[subpages depth="1" childof="286"]`

<div class="note">[subpages depth="1" childof="286"]</div>

***

If the page doesn't have any subpages it will display the following error for you to fix it:

`[subpages depth="1" childof="257"]]`

<div class="note">[subpages depth="1" childof="257"]</div>

### Usage

You can add the widget to your sidebar on Wordpress widgets page. There are 3 options:

{% include img.html img_src="/subpages-widget-options.jpg" width="250" height="277" %}

<ul>
	<li>Title: Title of the widget</li>
	<li>Exclude: Indexes of pages to be excluded. (Advanced use)</li>
	<li>Depth: Depth of index.</li>
</ul>

### Shortcode

The second, and more functional usage of plugin is the `[subpages]` shortcode. With no options given it will display subpages with no title, no exclusion and with a depth of 3. You can also use following examples to change the output:

* `[subpages depth="2"]` - show the list with a depth of 2.
* `[subpages exclude="2,4,12"]` - exclude subpages with indexes 2,4 and 12.
* `[subpages exclude="4" depth="0"]` - exclude post id 4 and show all subpages.
* `[subpages depth="1" childof="257"]` - show subpages of page with the Id of 257
* `[subpages depth="1" childof="257" exceptme="true"]` - add current page to the exclusions. This way you can show links to other subpages of parent easily. See the bottom of this post for a demonstration.

<a href="http://shailan.com/demo/subpages-extended/">See more shortcode examples on demo page &rarr;</a>

### Posts about Dropdown Menu Widget

{% include tagloop.html tag='subpages extended' %}
