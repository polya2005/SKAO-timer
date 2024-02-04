from gtts import gTTS

nextround = gTTS('เปลี่ยนฐาน', lang='th')
timeout = gTTS('หมดเวลา', lang='th')
oneminleft = gTTS('เหลือเวลาอีก 1 นาที', lang='th')

nextround.save('nextround.mp3')
timeout.save('timeout.mp3')
oneminleft.save('oneminleft.mp3')