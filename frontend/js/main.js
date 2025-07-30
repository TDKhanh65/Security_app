// Địa chỉ server đã deploy trên Render
const SERVER = 'https://security-app-pm25.onrender.com';

// Hàm xử lý mã hóa
async function encrypt() {
  const text = document.getElementById('text-encrypt').value.trim();
  const method = document.getElementById('method-encrypt').value;
  const key = document.getElementById('key-encrypt').value.trim();

  let body = { text };

  if (key) body.key = key;

  if (method === 'hoanvi') {
    body = { chuoi: text };
    try {
      body.thu_tu = JSON.parse(key);
    } catch {
      alert('❌ Khóa hoán vị phải là mảng JSON!, vd: [1, 2 , 3, ...]');
      return;
    }
  }

  try {
    const res = await fetch(`${SERVER}/encrypt/${method}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(body)
    });

    const data = await res.json();
    document.getElementById('result-encrypt').textContent =
      data.encrypted || data.error || '❌ Không mã hóa được!';
  } catch (err) {
    console.error('Lỗi mã hóa:', err);
    document.getElementById('result-encrypt').textContent =
      '❌ Không kết nối được với máy chủ!';
  }
}

// Hàm xử lý giải mã
async function decrypt() {
  const text = document.getElementById('text-decrypt').value.trim();
  const method = document.getElementById('method-decrypt').value;
  const key = document.getElementById('key-decrypt').value.trim();

  let body = { text };

  if (key) body.key = key;

  if (method === 'hoanvi') {
    body = { chuoi: text };
    try {
      body.thu_tu = JSON.parse(key);
    } catch {
      alert('❌ Khóa hoán vị phải là mảng JSON hợp lệ!');
      return;
    }
  }

  try {
    const res = await fetch(`${SERVER}/decrypt/${method}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(body)
    });

    const data = await res.json();
    document.getElementById('result-decrypt').textContent =
      data.decrypted || data.error || '❌ Không giải mã được!';
  } catch (error) {
    console.error('Lỗi giải mã:', error);
    document.getElementById('result-decrypt').textContent =
      '❌ Không kết nối được với máy chủ!';
  }
}
