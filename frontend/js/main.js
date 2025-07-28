async function encrypt() {
  const text = document.getElementById('text-encrypt').value;
  const method = document.getElementById('method-encrypt').value;
  const key = document.getElementById('key-encrypt').value;

  let body = { text };
  if (key) body.key = key;
  if (method === 'hoanvi') {
    body = { chuoi: text };
    try {
      body.thu_tu = JSON.parse(key);
    } catch {
      alert('❌ Khóa hoán vị phải là mảng JSON!');
      return;
    }
  }

  try {
    const res = await fetch(`http://localhost:5500/encrypt/${method}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(body)
    });
    const data = await res.json();
    document.getElementById('result-encrypt').textContent =
      data.encrypted || data.error || '❌ Không mã hóa được!';
  } catch {
    document.getElementById('result-encrypt').textContent = '❌ Không kết nối được với máy chủ!';
  }
}

async function decrypt() {
  const text = document.getElementById('text-decrypt').value;
  const method = document.getElementById('method-decrypt').value;
  const key = document.getElementById('key-decrypt').value;

  let body = { text };
  if (key) body.key = key;
  if (method === 'hoanvi') {
    body = { chuoi: text };
    try {
      body.thu_tu = JSON.parse(key);
    } catch {
      alert('❌ Khóa hoán vị phải là mảng JSON! ví dụ: [1, 0, 2]');
      return;
    }
  }

  try {
    const res = await fetch(`http://localhost:5500/decrypt/${method}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(body)
    });
    const data = await res.json();
    document.getElementById('result-decrypt').textContent =
      data.decrypted || data.error || '❌ Không giải mã được!';
  } catch {
    document.getElementById('result-decrypt').textContent = '❌ Không kết nối được với máy chủ!';
  }
}
// Hàm xử lý giải mã
async function decrypt() {
  const text = document.getElementById('text-decrypt').value.trim();
  const method = document.getElementById('method-decrypt').value;
  const key = document.getElementById('key-decrypt').value.trim();

  let body = { text };

  // Nếu có key thì thêm vào body
  if (key) body.key = key;

  // Riêng với hoán vị thì xử lý khác
  if (method === 'hoanvi') {
    body = { chuoi: text }; // Dùng trường 'chuoi' thay vì 'text'
    try {
      body.thu_tu = JSON.parse(key); // Khóa hoán vị phải là mảng JSON
    } catch {
      alert('❌ Khóa hoán vị phải là mảng JSON hợp lệ!');
      return;
    }
  }

  try {
    const res = await fetch(`http://localhost:5500/decrypt/${method}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(body)
    });

    const data = await res.json();

    document.getElementById('result-decrypt').textContent =
      data.decrypted || data.error || '❌ Không giải mã được!';
  } catch (error) {
    console.error('Giải mã lỗi:', error);
    document.getElementById('result-decrypt').textContent =
      '❌ Không kết nối được với máy chủ!';
  }
}

