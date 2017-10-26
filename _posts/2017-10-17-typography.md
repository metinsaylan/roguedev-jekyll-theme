---
title: Typography
---
In this sample post you can see various typographic elements.

# Heading 1

## Heading 1

### Heading 1

#### Heading 4

Here is a sample paragraph. That is quite long to show how simple paragraphs look like. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.

Once a wise man said:

> Cogito, Ergo Sum
Descartes

And this theme has some nice styles for code blocks too. Here is a snippet:

```php
function shailan_redirect_404() {
    global $wp_query;
    if ( $wp_query->is_404 ) {
      wp_redirect( get_bloginfo('wpurl'), 301 );
      exit;
    }
}
add_action('template_redirect', 'shailan_redirect_404', 1);
```
