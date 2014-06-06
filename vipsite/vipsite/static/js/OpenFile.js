function uploadAndSubmit(form) { 
 var thisform = form; 
    
 if (thisform["file"].files.length > 0) { 
 // Ѱ�ұ����е� <input type="file" ... /> ��ǩ
 var file = thisform["file"].files[0]; 
 // try sending 
 var reader = new FileReader(); 

 reader.onloadstart = function() { 
 // ����¼��ڶ�ȡ��ʼʱ����
 console.log("onloadstart"); 
 document.getElementById("bytesTotal").textContent = file.size; 
 } 
 reader.onprogress = function(p) { 
 // ����¼��ڶ�ȡ�����ж�ʱ����
 console.log("onprogress"); 
 document.getElementById("bytesRead").textContent = p.loaded; 
 } 

 reader.onload = function() { 
    // ����¼��ڶ�ȡ�ɹ������󴥷�
 console.log("load complete"); 
 } 

 reader.onloadend = function() { 
    // ����¼��ڶ�ȡ���������۳ɹ�����ʧ�ܶ��ᴥ��
 if (reader.error) { 
 console.log(reader.error); 
 } else { 
 document.getElementById("bytesRead").textContent = file.size; 
 // ���� XMLHttpRequest ���󣬷����ļ� Binary ����
 var xhr = new XMLHttpRequest(); 
 xhr.open(/* method */ "POST", 
 /* target url */ /*how do code? */  
 /*, async, default to true */); 
 xhr.overrideMimeType("application/octet-stream"); 
 xhr.sendAsBinary(reader.result); 
 xhr.onreadystatechange = function() { 
 if (xhr.readyState == 4) { 
 if (xhr.status == 200) { 
 console.log("upload complete"); 
 console.log("response: " + xhr.responseText); 
 } 
 } 
 } 
 } 
 } 

 reader.readAsBinaryString(file); 
 } else { 
 alert ("Please choose a file."); 
 } 
 } 