(function(){
  var btn=document.querySelector('.menu-btn'),nav=document.querySelector('.nav');
  if(btn&&nav){btn.addEventListener('click',function(){var o=nav.classList.toggle('open');btn.setAttribute('aria-expanded',o?'true':'false');});}
  document.querySelectorAll('.has-sub > button').forEach(function(b){
    b.addEventListener('click',function(e){e.stopPropagation();var li=b.parentNode,o=li.classList.toggle('open');b.setAttribute('aria-expanded',o?'true':'false');});
  });
  document.addEventListener('click',function(){document.querySelectorAll('.has-sub.open').forEach(function(li){li.classList.remove('open');li.querySelector('button').setAttribute('aria-expanded','false');});});
  var f=document.querySelector('form.f');
  if(f){
    var st=f.querySelector('.status'),endpoint=f.getAttribute('data-endpoint')||'';
    f.addEventListener('submit',function(e){
      e.preventDefault();
      if(f.querySelector('.hp input').value){return;}
      var name=f.name.value.trim(),email=f.email.value.trim(),msg=f.message.value.trim();
      if(!name||!email||!msg){st.textContent='Please fill in your name, email and message.';return;}
      if(!endpoint){
        var body='Name: '+name+'\nEmail: '+email+'\n\n'+msg;
        window.location.href='mailto:info@tccbss.com?subject='+encodeURIComponent('Website enquiry from '+name)+'&body='+encodeURIComponent(body);
        st.textContent='Your email app should open with the message ready to send. If it does not, write to info@tccbss.com.';
        return;
      }
      st.textContent='Sending…';
      fetch(endpoint,{method:'POST',headers:{'Accept':'application/json'},body:new FormData(f)}).then(function(r){
        if(r.ok){f.reset();st.textContent='Thank you. Your message has been sent and we will get back to you shortly.';}
        else{st.textContent='Sorry, the message could not be sent. Please email info@tccbss.com.';}
      }).catch(function(){st.textContent='Sorry, the message could not be sent. Please email info@tccbss.com.';});
    });
  }
})();
