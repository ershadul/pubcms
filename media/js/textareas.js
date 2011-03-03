tinyMCE.init({
	// General options
	mode : "textareas",
	theme : "advanced",
	plugins : "layer,table,advhr,advimage,advlink,emotions,iespell,inlinepopups,insertdatetime,media,searchreplace,print,contextmenu,paste,directionality,fullscreen,noneditable,visualchars,nonbreaking,xhtmlxtras,wordcount,advlist",

	// Theme options
	theme_advanced_buttons1 : "bold,italic,underline,strikethrough,|,justifyleft,justifycenter,justifyright,justifyfull,styleselect,formatselect,fontselect,fontsizeselect,fullscreen,code",
	theme_advanced_buttons2 : "cut,copy,paste,pastetext,|,search,replace,|,bullist,numlist,|,outdent,indent,blockquote,|,undo,redo,|,link,unlink,anchor,image,cleanup,|,insertdate,inserttime,forecolor,backcolor",
	theme_advanced_buttons3 : "tablecontrols,|,hr,removeformat,visualaid,|,sub,sup,|,charmap,emotions,iespell,media,advhr,|,print,|,ltr,rtl",

	theme_advanced_toolbar_location : "top",
	theme_advanced_toolbar_align : "left",
	theme_advanced_statusbar_location : "bottom",
	theme_advanced_resizing : true,

    theme_advanced_fonts : "SolaimanLipi,sans,serif,arial",
    theme_advanced_font_sizes : "12px,14px,16px,18px,20px,22px,24px,26px,28px,30px,36px,40px,46px",

	// Example content CSS (should be your site CSS)
	//content_css : "/media/js/time_mce/css/editor.css",

	//template_external_list_url : "lists/template_list.js",
	//external_link_list_url : "lists/link_list.js",
	//external_image_list_url : "lists/image_list.js",
	//media_external_list_url : "lists/media_list.js",

	width: '700',
	height: '400'

});