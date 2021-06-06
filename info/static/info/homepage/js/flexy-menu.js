
jQuery.fn.flexymenu = function(options){
	var settings = {
		 speed	 			: 300     				// dropdown speed (ms)
		,type	 			: "horizontal"    		// menu type arrangement
		,align	 			: "left"  				// menu alignment
		,indicator	 		: false     			// indicator that indicates a submenu
		,hideClickOut		: true     				// hide submenus when click outside menu
	}
	$.extend( settings, options );
	
	var bigScreen = false;
	var menu = $(this);
	var lastScreenWidth = window.innerWidth;
	
	if(settings.type == "vertical"){
		$(menu).addClass("vertical");
		if(settings.align == "right"){
			$(menu).addClass("right");
		}
	}
	
	
}
