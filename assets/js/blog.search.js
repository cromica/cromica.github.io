
	jQuery(function() {
    jQuery('#search-query').lunrSearch({
      indexUrl: '/js/index.json',             // URL of the `index.json` index data for your site
      results:  '#search-results',          // jQuery selector for the search results container
      entries:  '.entries',                 // jQuery selector for the element to contain the results list, must be a child of the results element above.
      template: '#search-results-template'  // jQuery selector for the Mustache.js template
    });
  });