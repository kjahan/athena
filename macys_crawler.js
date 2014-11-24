// Get Macys reviews

var page = require('webpage').create(),
url = 'http://www1.macys.com/shop/product/george-foreman-grp95r-grill-6-servings?ID=797879';
page.open(url, function (status) {
    if (status !== 'success') {
        console.log('Unable to access network');
    } else {
    	    var results = page.evaluate(function() {
	    var allSpans = document.getElementsByTagName('span');
	    var reviews = [];
	    for(var i = 0; i < allSpans.length; i++) {
                if(allSpans[i].className === 'BVRRReviewText') {
		    reviews.push(allSpans[i].innerHTML);
                }
            }
            return reviews;
    	    });
        console.log(results.join('\n'));
    }
    phantom.exit();
});
