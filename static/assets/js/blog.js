$(document).ready(function() {
	
	/* ======= Highlight.js Plugin ======= */ 
         
    $('pre code').each(function(i, block) {
	    hljs.highlightBlock(block);
	 });

});