# -*- coding: utf-8 -*-
def get_main_menu():
    main_menu = [
        {
            'name': 'current-issue',
            'title': u'চলতি সংখ্যা',
            'link': '/'
        },
        {
            'name': 'archive',
            'title': u'পুরোনো সংখ্যা',
            'link': '/archive'
        },

        {
            'name': 'section',
            'title': u'বিভাগ',
            'link': '/section'
        },
        {
            'name': 'about',
            'title': u'আমাদের কথা',
            'link': '/about'
        },

        {
            'name': 'contact',
            'title': u'যোগাযোগ',
            'link': '/contact'
        } ,
        {
            'name': 'feedback',
            'title': u'মতামত',
            'link': '/feedback'
        },
        {
            'name': 'rss_feed',
            'title': 'RSS',
            'link': '/feeds/rss/current'
        }
    ]
    return main_menu

locals = {
    'bismillah':  u'বিসমিল্লাহির রহমানির রহীম',
    'in_this_issue':   u'এই সংখ্যায় আছে'          ,
    'issue_year': u'প্রকাশনা',
    'number': u'সংখ্যা'    ,
    'written_by': 'লিখেছেনঃ'      ,
    'translated_by': u'অনুবাদঃ'              ,
    'home': u'হোম'                               ,
    'read_more': u'বিস্তারিত'   ,
    'all_articles': u'এই বিভাগের সকল লেখা'        ,
    'all_sections': u'সকল বিভাগ'        ,
    'section': u'বিভাগ'      ,
    'sub_section': u'উপ-বিভাগ'     ,
    'archive': u'পুরোনো সংখ্যা'   ,
    'other_sections': u'অন্যান্য বিভাগ'     ,
    'related_articles': u'অন্যান্য লেখা'    ,
    'top_articles': u'সর্বাধিক পঠিত',
	'name': u'নাম',
	'email': u'ইমেল (অবশ্যই ইংরেজিতে)',
	'feedback': u'মতামত (বাংলায় অগ্রগন্য)',
	'submit': u'প্রেরণ করুন',
	'math_question': u'নিচের যোগ বা বিয়োগ সংক্রান্ত প্রশ্নটির উত্তর দিন (অবশ্যই ইংরেজিতে)',
	'feedback_successful': u'আলহামদুলিল্লাহ! আপনার মূল্যবান মতামতটি সফলভাবে গৃহীত হয়েছে। আল্লাহ তাআলা আপনাকে উত্তম প্রতিদান দিন - আমীন।',
	'search': u'খুঁজুন',
	'search_help': u'বাংলা ইউনিকোডে টাইপ করুন। যেমন: কুরআন, তাওহীদ ইত্যাদি',
	'editor': u'সম্পাদক',
	'editor_name': u'মাওলানা আবু তাহের মিসবাহ',
	'dua_3': u'(দামাত বারাকাতাহুম) কর্তৃক সম্পাদিত',
	'publisher': u'[ একটি দারুল কলম প্রকাশনা ]' ,
	'print': u'প্রিন্ট',
	'share': u'শেয়ার করুন',
	'current_issue': u'চলতি সংখ্যা',
	'back_issue': u'পুরোনো সংখ্যা',
	'cover_image': u'প্রচ্ছদ',
	'next': u'পরবর্তী',
	'previous': u'পূর্ববর্তী',
	'search_result': u'অনুসন্ধানের ফলাফল',
	'part': u'পর্ব',
    'top': u'উপরে'
}
