var area = document.getElementById('chatspace');
var user = document.getElementById('user');
var closeReply = document.getElementById('closereply');
var sendMessageButton = document.getElementById('sendbutton')
var sendMessageBox = document.getElementById('sendbox');
var replyMessage = document.getElementById('replytext');
var event_name;
var logout_btn = document.getElementById('logout');
var requestLogout;

function loaded(){
  event_name = document.getElementById('event').innerHTML;
	firebase.database().ref(event_name+'/').on('child_added', function(snapshot) {
      var message = snapshot.val();
      var m = new MessageBox(message);
      m.attach();
	});
};
var MessageBox = function(message){
  this.parent = message.key;
  this.to = message.name;
  this.message = message.text;
  this.reply = message.reply;
  this.replyto = message.replyto;
  this.replybutton = document.createElement('A');
  this.replybutton.innerHTML = "Reply";
  this.replybutton.obj = this;
  this.replybutton.addEventListener("click",clickreg);
}

MessageBox.prototype.attach= function(){
  var messagebox = document.createElement('DIV');
  var messagehead = document.createElement('H1');
  var messagebody = document.createElement('SPAN');
  if(this.reply&&this.reply.length!=0){
    var replyhead = document.createElement('H2');
    var replybody = document.createElement('SPAN');
    var hr = document.createElement('HR');
    replyhead.innerHTML = this.replyto;
    replybody.innerHTML = this.reply;
    messagebox.appendChild(replyhead);
    messagebox.appendChild(replybody);
    messagebox.appendChild(hr);
  }
  messagehead.innerHTML = this.to;
  messagebody.innerHTML = this.message;
  messagebox.appendChild(messagehead);
  messagebox.appendChild(messagebody);
  messagebox.appendChild(this.replybutton);
  messagebox.setAttribute('class','message');
  area.appendChild(messagebox);
  var scrollpixel = messagebox.offsetTop;
  area.scrollTop = scrollpixel;
}

function clickreg(e){
  var element = e.target.obj;
  replyMessage.innerHTML = element.message;
  replyMessage.obj = element;
  closeReply.style.opacity = 1;
}


sendMessageButton.addEventListener("click",function(){
	var message = sendMessageBox.value;
  var element = replyMessage.obj;
  if(message){
    var sendData = {
      name: "admin",
      text : message,
    }
    if(element){
      sendData.replyto = element.to;
      sendData.reply = element.message;
    }
    else{
      sendData.reply = "";
      sendData.replyto = "";
    }
  	firebase.database().ref(event_name+'/').push(sendData);
    replyMessage.innerHTML = "";
    sendMessageBox.value = "";
    closeReply.style.opacity = 0;
  }
});

closeReply.addEventListener("click",function(e){
  replyMessage.innerHTML = "";
  delete replyMessage.obj;
  closeReply.style.opacity = 0;
});


logout.addEventListener("click",function(){
  requestLogout = new XMLHttpRequest();
  requestLogout.onreadystatechange = logmeout;
  requestLogout.open('POST','/admin/logout/',true);
  requestLogout.setRequestHeader('content-type','application/json');
  var admin_data = {
    event:event_name.innerHTML
  };
  requestLogout.send(JSON.stringify(admin_data));
});

function logmeout(){
  if(requestLogout.readyState == XMLHttpRequest.DONE){
    var response = JSON.parse(requestLogout.responseText);
    if(response.status)
      window.location.href="http://localhost:8000/admin/";
  }
}