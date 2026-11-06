const API_URL = 'http://127.0.0.1:5001';

const MOODS = [
  { id: 'angry', name: 'Angry', blurb: 'Rude and fired up',
    brows: 'M7 7l3 1.5M17 7l-3 1.5', mouth: 'M8.5 16c1-1.2 2.2-1.8 3.5-1.8s2.5.6 3.5 1.8',
    hello: 'What do you want now? Go on, spit it out.' },
  { id: 'friendly', name: 'Friendly', blurb: 'Warm and kind',
    brows: 'M0 0', mouth: 'M8 14c1 1.6 2.4 2.4 4 2.4s3-.8 4-2.4',
    hello: "Hey there! I'm so glad you stopped by. What's on your mind today?" },
  { id: 'funny', name: 'Funny', blurb: 'Jokes and humour',
    brows: 'M7 7.5c1-.8 2-.8 3 0M14 7.5c1-.8 2-.8 3 0', mouth: 'M7.5 13.5h9c0 3-2 5-4.5 5s-4.5-2-4.5-5z',
    hello: "Knock knock! Just kidding, you're already in. What's up?" },
  { id: 'sad', name: 'Sad', blurb: 'Soft and melancholy',
    brows: 'M7 8l3-1.5M17 8l-3-1.5', mouth: 'M8.5 16.5c1-1.2 2.2-1.8 3.5-1.8s2.5.6 3.5 1.8',
    hello: "Oh... hi. It's a little gloomy in here, but I'm listening." },
  { id: 'motivational', name: 'Motivational', blurb: 'Pep talks and push',
    brows: 'M7 6.5h3M14 6.5h3', mouth: 'M7.5 13.5c1.2 3.2 3 4.5 4.5 4.5s3.3-1.3 4.5-4.5',
    hello: "You showed up, and that's step one! What are we conquering today?" }
];

const moodsEl = document.getElementById('moods');
const messagesEl = document.getElementById('messages');
const moodNameEl = document.getElementById('moodName');
const avatarEl = document.getElementById('avatar');
const form = document.getElementById('form');
const input = document.getElementById('msg');
const clearBtn = document.getElementById('clearBtn');

let current = 'friendly';
let waiting = false;

function faceSvg(m) {
  return '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' +
    '<circle cx="12" cy="12" r="9"/><path d="' + m.brows + '"/><path d="M9 10h.01M15 10h.01"/><path d="' + m.mouth + '"/></svg>';
}

function addMessage(from, text) {
  const row = document.createElement('div');
  row.className = 'row ' + from;
  const bubble = document.createElement('div');
  bubble.className = 'bubble';
  bubble.textContent = text;
  row.appendChild(bubble);
  messagesEl.appendChild(row);
  messagesEl.scrollTop = messagesEl.scrollHeight;
  return bubble;
}

function renderMoods() {
  moodsEl.innerHTML = '';
  MOODS.forEach(function (m) {
    const btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'mood-btn' + (m.id === current ? ' active' : '');
    btn.setAttribute('aria-pressed', m.id === current ? 'true' : 'false');
    btn.innerHTML =
      '<span class="mood-icon">' + faceSvg(m) + '</span>' +
      '<span class="mood-text"><span class="mood-name">' + m.name + '</span>' +
      '<span class="mood-blurb">' + m.blurb + '</span></span>';
    btn.addEventListener('click', function () { setMood(m.id); });
    moodsEl.appendChild(btn);
  });
}

function setMood(id) {
  current = id;
  const m = MOODS.find(function (x) { return x.id === id; });
  moodNameEl.textContent = m.name + ' Chatbot';
  avatarEl.innerHTML = faceSvg(m);
  messagesEl.innerHTML = '';
  input.value = '';
  addMessage('bot', m.hello);
  renderMoods();

  // start a fresh conversation on the server for this mood
  fetch(API_URL + '/reset', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ mood: id })
  }).catch(function () { /* server may not be running yet */ });
}

form.addEventListener('submit', async function (e) {
  e.preventDefault();
  const text = input.value.trim();
  if (!text || waiting) return;

  addMessage('user', text);
  input.value = '';
  waiting = true;
  const thinking = addMessage('bot', '...');

  try {
    const res = await fetch(API_URL + '/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ mood: current, message: text })
    });
    const data = await res.json();
    thinking.textContent = data.reply || data.error || 'Something went wrong.';
  } catch (err) {
    thinking.textContent = 'Cannot reach the server. Is "python3 server.py" running?';
  }

  waiting = false;
  messagesEl.scrollTop = messagesEl.scrollHeight;
  input.focus();
});

clearBtn.addEventListener('click', function () { setMood(current); });

setMood(current);