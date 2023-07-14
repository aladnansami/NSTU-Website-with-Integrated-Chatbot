/* =================== DISPLAYING AND REMOVING CHATBOX =================== */
const message_bot_btn=document.getElementById("message-bot");
message_bot_btn.addEventListener("click",()=>{
  const chat_box=document.getElementsByClassName("boxed")[0];
  chat_box.style.right="15px";
})
const close_chat_box_btn=document.getElementsByClassName('close-icon')[0];
close_chat_box_btn.addEventListener("click",()=>{
  const chat_box=document.getElementsByClassName("boxed")[0];
  chat_box.style.right="-535px";
})

/* =================== HANDLING MICROPHONE =================== */
const textInput=document.getElementById("textInput");
const msger_send_btn=document.getElementById("msger-send-btn");
const mic_button=document.getElementById("mic_button")
mic_button.addEventListener("click",()=>{
  const recognition = new webkitSpeechRecognition();
  recognition.continuous = false;
  recognition.lang = 'en-US';
  recognition.interimResults = false;
  recognition.maxAlternatives = 1;

  recognition.onresult = function(event) {
    const transcript = event.results[0][0].transcript;
    textInput.value=transcript;
    setTimeout(()=>{},1000);
    msger_send_btn.click();
  };

  recognition.onerror = function(event) {
    console.error('Error occurred during speech recognition:', event.error);
  };

  recognition.start();
})



/* =================== HANDLING USER FEEDBACK =================== */
const feed_back_box=document.getElementById("feed_back_box");
feed_back_box.addEventListener("submit",(e)=>{
  e.preventDefault();
  const feed_back_msg=document.getElementsByName("feed_back_msg")[0].value;
  const feed_back_type=document.getElementsByName("feed_back_type")[0].value;
  $.post('/user_feedback',{feed_back_msg:feed_back_msg,feed_back_type:feed_back_type})
  document.getElementsByClassName("close_feedback_box")[0].click()
})


/* =================== HANDLING CHATBOT RESPONSE =================== */
const msgerForm = get(".msger-inputarea");
const msgerInput = get(".msger-input");
const msgerChat = get(".msger-chat");

// const BOT_IMG = "{{ url_for('static',filename='./images/bot.png') }}";
// const PERSON_IMG = "{{ url_for('static',filename='./images/avatar.png') }}";
const BOT_IMG = "/static/images/bot.png";
const PERSON_IMG = "/static/images/avatar.png";
const BOT_NAME = "Student Information Chatbot";
const PERSON_NAME = "You";

function get(selector, root = document) {
  return root.querySelector(selector);
}

function formatDate(date) {
  const h = "0" + date.getHours();
  const m = "0" + date.getMinutes();
  return `${h.slice(-2)}:${m.slice(-2)}`;
}

function botResponse(rawText) {
  $.get("/get", { msg: rawText }).done(function (data) {
    const msgText = data;
    console.log(msgText)
    appendBotMessage(BOT_NAME, BOT_IMG, "left", msgText);
  });
}

function appendUserMessage(name, img, side, text) {
  const msgHTML = `
    <div class="msg ${side}-msg">
      <div class="msg-img" style="background-image: url(${img})"></div>
      <div class="msg-bubble">
        <div class="msg-info">
          <div class="msg-info-name">${name}</div>
          <div class="msg-info-time">${formatDate(new Date())}</div>
        </div>
        <div class="msg-text">${text}</div>
      </div>
    </div>`;

  msgerChat.insertAdjacentHTML("beforeend", msgHTML);
  msgerChat.scrollTop += 500;
}

function appendBotMessage(name, img, side, text) {
  const msgHTML = `
    <div class="msg ${side}-msg">
      <div class="msg-img" style="background-image: url(${img})"></div>
      <div class="msg-bubble">
        <div class="msg-info">
          <div class="msg-info-name">${name}</div>
          <div class="msg-info-time">${formatDate(new Date())}</div>
        </div>
        <div class="msg-text">${text}</div>
        <div class="feed_back_button">
            <button type="submit" class="like_button"><i class="fa-solid fa-thumbs-up" data-toggle="modal" data-target="#PosfeedBackBox"></i></button>
            <button type="submit" class="dislike_button"><i class="fa-solid fa-thumbs-down" data-toggle="modal" data-target="#NegfeedBackBox"></i></button>
        </div>
      </div>
    </div>`;

  msgerChat.insertAdjacentHTML("beforeend", msgHTML);
  msgerChat.scrollTop += 500;
}

msgerForm.addEventListener("submit", event => {
  event.preventDefault();
  const msgText = msgerInput.value;
  if (!msgText) return;
  
  appendUserMessage(PERSON_NAME, PERSON_IMG, "right", msgText);
  msgerInput.value = "";
  botResponse(msgText);
});

/* =================== HOVER LIST ========================*/ 
const hover_list_container = document.getElementsByClassName('hover-list-container');
console.log(hover_list_container)
Array.from(hover_list_container).forEach((item) => {
  item.addEventListener("click", () => {
    Array.from(hover_list_container).forEach((i) => {
      i.getElementsByClassName("hover-list-item")[0].style.display="none";
    })
    if(item.getElementsByClassName("hover-list-item")[0].style.display=="block"){
      item.getElementsByClassName("hover-list-item")[0].style.display="none";
    }else{
      item.getElementsByClassName("hover-list-item")[0].style.display="block";
    }
  })
})









