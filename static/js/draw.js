// document.addEventListener('DOMContentLoaded', function() {
// const canvas = document.getElementById('canvas');
// const ctx = canvas.getContext('2d');
// let isDrawing = false;

// canvas.addEventListener('mousedown', (e) => {
//     isDrawing = true;
//     draw(e);
// });

// canvas.addEventListener('mousemove', (e) => {
//     if (isDrawing) {
//         draw(e);
//     }
// });

// canvas.addEventListener('mouseup', () => {
//     isDrawing = false;
// });

// function draw(e) {
//     const rect = canvas.getBoundingClientRect();
//     const x = e.clientX - rect.left;
//     const y = e.clientY - rect.top;

//     ctx.fillStyle = '#000';
//     ctx.fillRect(x, y, 10, 10);
// }

// document.getElementById('predictBtn').addEventListener('click', () => {
//     const imageData = canvas.toDataURL('image/png');
//     fetch('/predict', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/x-www-form-urlencoded'
//         },
//         body: `imageData=${imageData}`
//     })
//     .then(response => response.json())
//     .then(data => {
//         document.getElementById('result').textContent = `Predicted Character: ${data.character}`;
//     })
//     .catch(error => {
//         console.error('Error:', error);
//     });
// });

// });

// const canvas = document.getElementById('canvas');
// const ctx = canvas.getContext('2d');
// let isDrawing = false;

// canvas.addEventListener('mousedown', (e) => {
//     isDrawing = true;
//     draw(e);
// });

// canvas.addEventListener('mousemove', (e) => {
//     if (isDrawing) {
//         draw(e);
//     }
// });

// canvas.addEventListener('mouseup', () => {
//     isDrawing = false;
// });

// function draw(e) {
//     const rect = canvas.getBoundingClientRect();
//     const x = e.clientX - rect.left;
//     const y = e.clientY - rect.top;

//     ctx.fillStyle = '#000';
//     ctx.fillRect(x, y, 10, 10);
// }

// document.getElementById('predictBtn').addEventListener('click', () => {
//     const imageData = canvas.toDataURL('image/png');
//     fetch('/predict', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/x-www-form-urlencoded'
//         },
//         body: `imageData=${imageData}`
//     })
//     .then(response => response.json())
//     .then(data => {
//         document.getElementById('result').textContent = `Predicted Character: ${data.character}`;
//     })
//     .catch(error => {
//         console.error('Error:', error);
//     });
// });

// const canvas = document.getElementById('canvas');
// const ctx = canvas.getContext('2d');
// let isDrawing = false;

// canvas.addEventListener('mousedown', (e) => {
//     isDrawing = true;
//     draw(e);
// });

// canvas.addEventListener('mousemove', (e) => {
//     if (isDrawing) {
//         draw(e);
//     }
// });

// canvas.addEventListener('mouseup', () => {
//     isDrawing = false;
// });

// function draw(e) {
//     const rect = canvas.getBoundingClientRect();
//     const x = e.clientX - rect.left;
//     const y = e.clientY - rect.top;

//     ctx.fillStyle = '#000';
//     ctx.fillRect(x, y, 10, 10);
// }

// document.getElementById('predictBtn').addEventListener('click', () => {
//     const imageData = canvas.toDataURL('image/png').replace(/^data:image\/(png|jpg);base64,/, '');
//     fetch('/predict', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/x-www-form-urlencoded'
//         },
//         body: `imageData=${encodeURIComponent(imageData)}`
//     })
//     .then(response => response.json())
//     .then(data => {
//         document.getElementById('result').textContent = `Predicted Character: ${data.character}`;
//     })
//     .catch(error => {
//         console.error('Error:', error);
//     });
// });

const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');
let isDrawing = false;

canvas.addEventListener('mousedown', (e) => {
    isDrawing = true;
    draw(e);
});

canvas.addEventListener('mousemove', (e) => {
    if (isDrawing) {
        draw(e);
    }
});

canvas.addEventListener('mouseup', () => {
    isDrawing = false;
});

function draw(e) {
    const rect = canvas.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;

    ctx.fillStyle = '#000';
    ctx.fillRect(x, y, 10, 10);
}

// document.getElementById('predictBtn').addEventListener('click', () => {
//     const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
//     const pixelData = imageData.data;
//     // Extract raw pixel data and send it for prediction
//     fetch('/predict', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/x-www-form-urlencoded'
//         },
//         body: `imageData=${pixelData}`
//     })
//     .then(response => response.json())
//     .then(data => {
//         document.getElementById('result').textContent = `Predicted Character: ${data.character}`;
//     })
//     .catch(error => {
//         console.error('Error:', error);
//     });
// });
// document.getElementById('predictBtn').addEventListener('click', () => {
//     const imageData = canvas.toDataURL('image/png');
//     // Use the base64 image data for prediction
//     fetch('/predict', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/x-www-form-urlencoded'
//         },
//         body: `imageData=${encodeURIComponent(imageData)}`
//     })
//     .then(response => response.json())
//     .then(data => {
//         document.getElementById('result').textContent = `Predicted Character: ${data.character}`;
//     })
//     .catch(error => {
//         console.error('Error:', error);
//     });
// });


document.getElementById('predictBtn').addEventListener('click', () => {
    const imageData = canvas.toDataURL('image/png');
    // Use the base64 image data for prediction
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: `imageData=${encodeURIComponent(imageData)}`
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').textContent = `Predicted Character: ${data.character}`;
    })
});

