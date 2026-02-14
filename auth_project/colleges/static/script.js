/* ===================================
   🔎 LIVE SEARCH FILTER (LOCAL)
=================================== */
function searchCollege(){
let input=document.getElementById("searchInput").value.toLowerCase();
let cards=document.querySelectorAll(".card");

cards.forEach(card=>{
let text=card.innerText.toLowerCase();
card.style.display=text.includes(input)?"block":"none";
});

// 🧠 ALSO CALL REAL AI SUGGESTIONS
fetch(`/ai-chat/?q=${input}`)
.then(res=>res.json())
.then(data=>{
console.log("AI Suggestions:",data);
});
}


/* ===================================
   🎯 FILTER BUTTONS (IIT/NIT/IIIT)
=================================== */
function filterType(type){
let cards=document.querySelectorAll(".card");

cards.forEach(card=>{
let text=card.innerText;
card.style.display = text.includes(type) || type=="" ? "block":"none";
});
}


/* ===================================
   💎 3D HOVER EFFECT
=================================== */
document.addEventListener("DOMContentLoaded",()=>{

document.querySelectorAll(".card").forEach(card=>{

card.addEventListener("mousemove",(e)=>{
let x=(e.offsetX/card.offsetWidth - 0.5)*10;
let y=(e.offsetY/card.offsetHeight - 0.5)*10;
card.style.transform=`rotateY(${x}deg) rotateX(${y}deg) scale(1.05)`;
});

card.addEventListener("mouseleave",()=>{
card.style.transform="rotateY(0) rotateX(0)";
});

});

});


/* ===================================
   🧠 REAL AI CHATBOT (DJANGO DB)
=================================== */
function sendAI(){

let msg=document.getElementById("aiInput").value;

fetch(`/ai-chat/?q=${msg}`)
.then(res=>res.json())
.then(data=>{

let reply=document.getElementById("aiReply");

if(typeof data.data === "string"){
reply.innerText=data.data;
return;
}

// 🔥 FORMAT REAL RESULTS
let text="";

data.data.forEach(c=>{
text += `✨ ${c.name} (${c.location})\n💰 Fees: ${c.fees}\n📊 Avg Package: ${c.avg}\n\n`;
});

reply.innerText=text;

});

}


/* ===================================
   🌐 SPA NAVIGATION (NO PAGE RELOAD)
=================================== */
document.addEventListener("click",function(e){

let link=e.target.closest(".spa-link");

if(link){

e.preventDefault();

let url=link.getAttribute("href");

fetch(url)
.then(res=>res.text())
.then(html=>{

let parser=new DOMParser();
let doc=parser.parseFromString(html,"text/html");

let newContent=doc.querySelector(".cosmic-container");

if(newContent){
document.querySelector(".cosmic-container").innerHTML=newContent.innerHTML;
window.history.pushState({}, "", url);
}

});

}

});


/* ===================================
   🌌 COSMIC PAGE ENTER ANIMATION
=================================== */
window.addEventListener("load",()=>{
document.body.style.opacity="1";
});
