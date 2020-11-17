# Http_requests.py

import requests
url = "http://www.google.com"
response = requests.get("http://www.google.com")

print(f"your request to {url} came back with status code {response.status_code}")

# your request to http://www.google.com came back with status code 200

print(response.text)
'''
your request to http://www.google.com came back with status code 200
<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="en-CA"><head><meta content="text/html; charset=UTF-8" http-equiv="Content-Type"><meta content="/images/branding/googleg/1x/googleg_standard_color_128dp.png" itemprop="image"><title>Google</title><script nonce="RwNBaomEHqtxDQn6bWKe3g==">(function(){window.google={kEI:'gAKFX7H2EYnr_QbVgbiACQ',kEXPI:'0,202162,1151585,5662,731,223,3110,547,1447,207,2415,789,10,1226,364,1499,612,205,383,246,5,1354,648,640,2811,315,3,66,593,391,283,869,110,102,352,319,97,129,189,990,99,199,322,701,49,1117489,1197713,569,8,328977,13677,4854,32693,16114,6057,11387,11240,9188,8384,4858,1362,9290,3021,4747,7,11026,1808,4020,978,7931,5297,2054,920,873,4200,6422,14528,4517,1398,1379,919,2277,10,2794,1593,1279,2214,528,149,1103,840,517,1466,56,4258,312,1136,3,2063,606,2023,1777,143,378,1946,2229,93,328,1284,16,2927,2246,1813,1787,3227,2845,7,6068,6286,4455,641,6134,1742,4929,108,3407,908,2,940,2615,2399,7468,1705,1570,3,346,230,970,44,1,820,4625,150,3499,1461,1028,6194,130,1661,4,498,643,111,276,2304,1236,271,874,405,805,4,1051,2393,74,1436,281,52,214,2163,464,459,1555,3849,218,1036,1315,3,2108,298,874,1426,69,1320,1095,200,2070,742,1752,690,1968,1395,2848,518,912,564,689,431,30,1303,2551,139,2447,647,786,204,52,1775,1255,256,2213,850,80,467,908,638,146,519,3,956,360,115,2,567,1008,517,1537,740,283,327,38,954,1369,55,745,3575,265,773,2,44,837,319,90,140,174,413,11,350,336,45,42,22,601,112,225,24,1406,282,96,117,1283,16,1057,96,427,43,634,831,376,253,187,491,100,210,2,1,3,83,2,332,884,297,120,1262,525,4,230,341,99,39,238,14,43,1811,474,118,5748276,3701,4,5997329,2800881,549,333,444,1,2,80,1,900,896,1,9,2,2551,1,748,141,59,736,563,1,4265,1,1,2,1017,9,305,3299,248,595,1,282,151,468,8,30,3,3,4,2,14,1,53,23959242,2716137,12107',kBL:'pDxO'};google.sn='webhp';google.kHL='en-CA';})();(function(){google.lc=[];google.li=0;google.getEI=function(a){for(var c;a&&(!a.getAttribute||!(c=a.getAttribute("eid")));)a=a.parentNode;return c||google.kEI};google.getLEI=function(a){for(var c=null;a&&(!a.getAttribute||!(c=a.getAttribute("leid")));)a=a.parentNode;return c};google.ml=function(){return null};google.time=function(){return Date.now()};google.log=function(a,c,b,d,g){if(b=google.logUrl(a,c,b,d,g)){a=new Image;var e=google.lc,f=google.li;e[f]=a;a.onerror=a.onload=a.onabort=function(){delete e[f]};google.vel&&google.vel.lu&&google.vel.lu(b);a.src=b;google.li=f+1}};google.logUrl=function(a,c,b,d,g){var e="",f=google.ls||"";b||-1!=c.search("&ei=")||(e="&ei="+google.getEI(d),-1==c.search("&lei=")&&(d=google.getLEI(d))&&(e+="&lei="+d));d="";!b&&google.cshid&&-1==c.search("&cshid=")&&"slh"!=a&&(d="&cshid="+google.cshid);b=b||"/"+(g||"gen_204")+"?atyp=i&ct="+a+"&cad="+c+e+f+"&zx="+google.time()+d;/^http:/i.test(b)&&"https:"==window.location.protocol&&(google.ml(Error("a"),!1,{src:b,glmm:1}),b="");return b};}).call(this);(function(){google.y={};google.x=function(a,b){if(a)var c=a.id;else{do c=Math.random();while(google.y[c])}google.y[c]=[a,b];return!1};google.lm=[];google.plm=function(a){google.lm.push.apply(google.lm,a)};google.lq=[];google.load=function(a,b,c){google.lq.push([[a],b,c])};google.loadAll=function(a,b){google.lq.push([a,b])};}).call(this);google.f={};(function(){
document.documentElement.addEventListener("submit",function(b){var a;if(a=b.target){var c=a.getAttribute("data-submitfalse");a="1"==c||"q"==c&&!a.elements.q.value?!0:!1}else a=!1;a&&(b.preventDefault(),b.stopPropagation())},!0);document.documentElement.addEventListener("click",function(b){var a;a:{for(a=b.target;a&&a!=document.documentElement;a=a.parentElement)if("A"==a.tagName){a="1"==a.getAttribute("data-nohref");break a}a=!1}a&&b.preventDefault()},!0);}).call(this);
var a=window.location,b=a.href.indexOf("#");if(0<=b){var c=a.href.substring(b+1);/(^|&)q=/.test(c)&&-1==c.indexOf("#")&&a.replace("/search?"+c.replace(/(^|&)fp=[^&]*/g,"")+"&cad=h")};</script><style>#gbar,#guser{font-size:13px;padding-top:1px !important;}#gbar{height:22px}#guser{padding-bottom:7px !important;text-align:right}.gbh,.gbd{border-top:1px solid #c9d7f1;font-size:1px}.gbh{height:0;position:absolute;top:24px;width:100%}@media all{.gb1{height:22px;margin-right:.5em;vertical-align:top}#gbar{float:left}}a.gb1,a.gb4{text-decoration:underline !important}a.gb1,a.gb4{color:#00c !important}.gbi .gb4{color:#dd8e27 !important}.gbf .gb4{color:#900 !important}
</style><style>body,td,a,p,.h{font-family:arial,sans-serif}body{margin:0;overflow-y:scroll}#gog{padding:3px 8px 0}td{line-height:.8em}.gac_m td{line-height:17px}form{margin-bottom:20px}.h{color:#36c}.q{color:#00c}em{font-weight:bold;font-style:normal}.lst{height:25px;width:496px}.gsfi,.lst{font:18px arial,sans-serif}.gsfs{font:17px arial,sans-serif}.ds{display:inline-box;display:inline-block;margin:3px 0 4px;margin-left:4px}input{font-family:inherit}body{background:#fff;color:#000}a{color:#11c;text-decoration:none}a:hover,a:active{text-decoration:underline}.fl a{color:#36c}a:visited{color:#551a8b}.sblc{padding-top:5px}.sblc a{display:block;margin:2px 0;margin-left:13px;font-size:11px}.lsbb{background:#eee;border:solid 1px;border-color:#ccc #999 #999 #ccc;height:30px}.lsbb{display:block}#WqQANb a{display:inline-block;margin:0 12px}.lsb{background:url(/images/nav_logo229.png) 0 -261px repeat-x;border:none;color:#000;cursor:pointer;height:30px;margin:0;outline:0;font:15px arial,sans-serif;vertical-align:top}.lsb:active{background:#ccc}.lst:focus{outline:none}</style><script nonce="RwNBaomEHqtxDQn6bWKe3g=="></script></head><body bgcolor="#fff"><script nonce="RwNBaomEHqtxDQn6bWKe3g==">(function(){var src='/images/nav_logo229.png';var iesg=false;document.body.onload = function(){window.n && window.n();if (document.images){new Image().src=src;}     
if (!iesg){document.f&&document.f.q.focus();document.gbqf&&document.gbqf.q.focus();}
}
})();</script><div id="mngb"><div id=gbar><nobr><b class=gb1>Search</b> <a class=gb1 href="http://www.google.ca/imghp?hl=en&tab=wi">Images</a> <a class=gb1 href="http://maps.google.ca/maps?hl=en&tab=wl">Maps</a> <a class=gb1 href="https://play.google.com/?hl=en&tab=w8">Play</a> <a class=gb1 href="http://www.youtube.com/?gl=CA&tab=w1">YouTube</a> <a class=gb1 href="https://news.google.com/?tab=wn">News</a> <a class=gb1 href="https://mail.google.com/mail/?tab=wm">Gmail</a> <a class=gb1 href="https://drive.google.com/?tab=wo">Drive</a> <a class=gb1 style="text-decoration:none" href="https://www.google.ca/intl/en/about/products?tab=wh"><u>More</u> &raquo;</a></nobr></div><div id=guser width=100%><nobr><span id=gbn class=gbi></span><span id=gbf class=gbf></span><span id=gbe></span><a href="http://www.google.ca/history/optout?hl=en" class=gb4>Web History</a> | <a  href="/preferences?hl=en" class=gb4>Settings</a> | <a target=_top id=gb_70 href="https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=http://www.google.com/&ec=GAZAAQ" class=gb4>Sign in</a></nobr></div><div class=gbh style=left:0></div><div class=gbh style=right:0></div></div><center><br clear="all" id="lgpd"><div id="lga"><img alt="Google" height="92" src="/images/branding/googlelogo/1x/googlelogo_white_background_color_272x92dp.png" style="padding:28px 0 14px" width="272" id="hplogo"><br><br></div><form action="/search" name="f"><table cellpadding="0" cellspacing="0"><tr valign="top"><td width="25%">&nbsp;</td><td align="center" nowrap=""><input name="ie" value="ISO-8859-1" type="hidden"><input value="en-CA" name="hl" type="hidden"><input name="source" type="hidden" value="hp"><input name="biw" type="hidden"><input name="bih" type="hidden"><div class="ds" style="height:32px;margin:4px 0"><input class="lst" style="margin:0;padding:5px 8px 0 6px;vertical-align:top;color:#000" autocomplete="off" value="" title="Google Search" maxlength="2048" name="q" size="57"></div><br style="line-height:0"><span class="ds"><span class="lsbb"><input class="lsb" value="Google Search" name="btnG" type="submit"></span></span><span class="ds"><span class="lsbb"><input class="lsb" id="tsuid1" value="I'm Feeling Lucky" name="btnI" type="submit"><script nonce="RwNBaomEHqtxDQn6bWKe3g==">(function(){var id='tsuid1';document.getElementById(id).onclick = function(){if (this.form.q.value){this.checked = 1;if (this.form.iflsig)this.form.iflsig.disabled = false;}
else top.location='/doodles/';};})();</script><input value="AINFCbYAAAAAX4UQkHr0FZE7tHTMezN8TXX2Qd_jljCZ" name="iflsig" type="hidden"></span></span></td><td class="fl sblc" align="left" nowrap="" width="25%"><a href="/advanced_search?hl=en-CA&amp;authuser=0">Advanced search</a></td></tr></table><input id="gbv" name="gbv" type="hidden" value="1"><script nonce="RwNBaomEHqtxDQn6bWKe3g==">(function(){var a,b="1";if(document&&document.getElementById)if("undefined"!=typeof XMLHttpRequest)b="2";else if("undefined"!=typeof ActiveXObject){var c,d,e=["MSXML2.XMLHTTP.6.0","MSXML2.XMLHTTP.3.0","MSXML2.XMLHTTP","Microsoft.XMLHTTP"];for(c=0;d=e[c++];)try{new ActiveXObject(d),b="2"}catch(h){}}a=b;if("2"==a&&-1==location.search.indexOf("&gbv=2")){var f=google.gbvu,g=document.getElementById("gbv");g&&(g.value=a);f&&window.setTimeout(function(){location.href=f},0)};}).call(this);</script></form><div id="gac_scont"></div><div style="font-size:83%;min-height:3.5em"><br><div id="gws-output-pages-elements-homepage_additional_languages__als"><style>#gws-output-pages-elements-homepage_additional_languages__als{font-size:small;margin-bottom:24px}#SIvCob{display:inline-block;line-height:28px;}#SIvCob a{padding:0 3px;}.H6sW5{display:inline-block;margin:0 2px;white-space:nowrap}.z4hgWe{display:inline-block;margin:0 2px}</style><div id="SIvCob">Google offered in:  <a href="http://www.google.com/setprefs?sig=0_IhIOCgzGXgul-7sFNGNfPBMw7o0%3D&amp;hl=fr&amp;source=homepage&amp;sa=X&amp;ved=0ahUKEwixtqiLtbDsAhWJdd8KHdUADpAQ2ZgBCAU">Français</a>  </div></div></div><span id="footer"><div style="font-size:10pt"><div style="margin:19px auto;text-align:center" id="WqQANb"><a href="/intl/en/ads/">Advertising Programs</a><a href="/services/">Business Solutions</a><a href="/intl/en/about.html">About Google</a><a href="http://www.google.com/setprefdomain?prefdom=CA&amp;prev=http://www.google.ca/&amp;sig=K_5tkJPYRZI6e6hkt6XtiJ_Ib6ojg%3D">Google.ca</a></div></div><p style="font-size:8pt;color:#767676">&copy; 2020 - <a href="/intl/en/policies/privacy/">Privacy</a> - <a href="/intl/en/policies/terms/">Terms</a></p></span></center><script nonce="RwNBaomEHqtxDQn6bWKe3g==">(function(){window.google.cdo={height:0,width:0};(function(){var a=window.innerWidth,b=window.innerHeight;if(!a||!b){var c=window.document,d="CSS1Compat"==c.compatMode?c.documentElement:c.body;a=d.clientWidth;b=d.clientHeight}a&&b&&(a!=google.cdo.width||b!=google.cdo.height)&&google.log("","","/client_204?&atyp=i&biw="+a+"&bih="+b+"&ei="+google.kEI);}).call(this);})();(function(){var u='/xjs/_/js/k\x3dxjs.hp.en.r2II1QmtVvQ.O/m\x3dsb_he,d/am\x3dAJ4gDg/d\x3d1/rs\x3dACT90oFQsc664dXJU65LcRLiL2Z6zw-mmg';
setTimeout(function(){var b=document;var a="SCRIPT";"application/xhtml+xml"===b.contentType&&(a=a.toLowerCase());a=b.createElement(a);a.src=u;google.timers&&google.timers.load&&google.tick&&google.tick("load","xjsls");document.body.appendChild(a)},0);})();(function(){window.google.xjsu='/xjs/_/js/k\x3dxjs.hp.en.r2II1QmtVvQ.O/m\x3dsb_he,d/am\x3dAJ4gDg/d\x3d1/rs\x3dACT90oFQsc664dXJU65LcRLiL2Z6zw-mmg';})();function _DumpException(e){throw e;}
function _F_installCss(c){}
(function(){google.jl={dw:false,em:[],emw:false,lls:'default',pdt:0,snet:true,uwp:true};})();(function(){var pmc='{\x22d\x22:{},\x22sb_he\x22:{\x22agen\x22:true,\x22cgen\x22:true,\x22client\x22:\x22heirloom-hp\x22,\x22dh\x22:true,\x22dhqt\x22:true,\x22ds\x22:\x22\x22,\x22ffql\x22:\x22en\x22,\x22fl\x22:true,\x22host\x22:\x22google.com\x22,\x22isbh\x22:28,\x22jsonp\x22:true,\x22msgs\x22:{\x22cibl\x22:\x22Clear Search\x22,\x22dym\x22:\x22Did you mean:\x22,\x22lcky\x22:\x22I\\u0026#39;m Feeling 
Lucky\x22,\x22lml\x22:\x22Learn more\x22,\x22oskt\x22:\x22Input tools\x22,\x22psrc\x22:\x22This search was removed from your \\u003Ca href\x3d\\\x22/history\\\x22\\u003EWeb History\\u003C/a\\u003E\x22,\x22psrl\x22:\x22Remove\x22,\x22sbit\x22:\x22Search by image\x22,\x22srch\x22:\x22Google Search\x22},\x22nrft\x22:false,\x22ovr\x22:{},\x22pq\x22:\x22\x22,\x22refpd\x22:true,\x22rfs\x22:[],\x22sbpl\x22:16,\x22sbpr\x22:16,\x22scd\x22:10,\x22stok\x22:\x22Wedcp49hSLyejCskkpnB67oq2wc\x22,\x22uhde\x22:false}}';google.pmc=JSON.parse(pmc);})();</script>        </body></html>
PS D:\MY STUFF\Online courses\Python\FirstProgram> 
'''