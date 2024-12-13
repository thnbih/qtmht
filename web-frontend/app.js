document.getElementById("tra-cuu-form").addEventListener("submit", async function (e) {
    e.preventDefault();
  
    const maSV = document.getElementById("ma-sv").value;
    const ketQuaDiv = document.getElementById("ket-qua");
  
    try {
      const response = await fetch(`http://localhost:5000/tra-cuu?ma_sinh_vien=${maSV}`);
      const data = await response.json();
  
      if (response.ok) {
        ketQuaDiv.innerHTML = `<p>Mã số sinh viên: ${data.ma_sinh_vien}</p>
                               <p>Điểm: ${data.diem}</p>`;
      } else {
        ketQuaDiv.innerHTML = `<p style="color: red;">${data.error}</p>`;
      }
    } catch (error) {
        ketQuaDiv.innerHTML = `<p style="color: red;">Không thể kết nối tới máy chủ. Lỗi: ${error.message}</p>`;
      }      
  });
  