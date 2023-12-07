css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://i.pinimg.com/originals/f0/48/9c/f0489ceb101a4bb4f8fd6f6f2c9e2762.jpg" >
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://imgs.search.brave.com/VsEyjlWFUIEuCGuuX6d1v1K0bI-18zhh7RFWDRj_5Q8/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9pY29u/cy52ZXJ5aWNvbi5j/b20vcG5nLzEyOC9o/YXJkd2FyZS9qYWNr/ZGl6aHVfcGMvdXNl/ci0xMTkucG5n">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''