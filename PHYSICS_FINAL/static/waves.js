document.addEventListener('DOMContentLoaded', function() {
    // Get DOM elements
    const waveTypeSelect = document.getElementById('waveType');
    const amplitudeSlider = document.getElementById('amplitude');
    const frequencySlider = document.getElementById('frequency');
    const wavelengthSlider = document.getElementById('wavelength');
    const amplitudeValue = document.getElementById('amplitudeValue');
    const frequencyValue = document.getElementById('frequencyValue');
    const wavelengthValue = document.getElementById('wavelengthValue');
    const waveCanvas = document.getElementById('waveCanvas');
    const calcWavelength = document.getElementById('calcWavelength');
    const calcFrequency = document.getElementById('calcFrequency');
    const calcAmplitude = document.getElementById('calcAmplitude');
    const calculateBtn = document.getElementById('calculateBtn');
    const resultsContainer = document.getElementById('resultsContainer');
    const darkModeToggle = document.getElementById('darkModeToggle');
    const solidBtn = document.getElementById('solidBtn');
    const liquidBtn = document.getElementById('liquidBtn');
    const gasBtn = document.getElementById('gasBtn');
    const waveLabels = document.querySelectorAll('.control-group label, .control-group span');
    const waveSpeedLabel = document.getElementById('waveSpeedLabel');
    const canvasLabels = document.createElement('div');
    canvasLabels.className = 'canvas-labels';
    waveCanvas.parentElement.appendChild(canvasLabels);
    // Set up canvas
    const ctx = waveCanvas.getContext('2d');
    waveCanvas.width = waveCanvas.parentElement.clientWidth;
    waveCanvas.height = 300;
    // Add these at the top with other DOM elements
const dopplerSourceSpeed = document.getElementById('dopplerSourceSpeed');
const dopplerObserverSpeed = document.getElementById('dopplerObserverSpeed');
const dopplerWaveSpeed = document.getElementById('dopplerWaveSpeed');
const dopplerSourceFreq = document.getElementById('dopplerSourceFreq');
const dopplerSourceSpeedValue = document.getElementById('dopplerSourceSpeedValue');
const dopplerObserverSpeedValue = document.getElementById('dopplerObserverSpeedValue');
const dopplerWaveSpeedValue = document.getElementById('dopplerWaveSpeedValue');
const dopplerSourceFreqValue = document.getElementById('dopplerSourceFreqValue');
const observedFreq = document.getElementById('observedFreq');
const freqChange = document.getElementById('freqChange');
const dopplerCanvas = document.getElementById('dopplerCanvas');
const dopplerCtx = dopplerCanvas.getContext('2d');
const dopplerSource = document.getElementById('dopplerSource');
const dopplerObserver = document.getElementById('dopplerObserver');

// Doppler parameters
let dopplerParams = {
    sourceSpeed: 0,
    observerSpeed: 0,
    waveSpeed: 343,
    sourceFreq: 440,
    sourceX: 0.2,
    observerX: 0.8,
    wavePhase: 0,
    waves: []
};

// Initialize Doppler canvas
function initDopplerCanvas() {
    dopplerCanvas.width = dopplerCanvas.parentElement.clientWidth;
    dopplerCanvas.height = 100;
}

// Update Doppler effect
function updateDopplerEffect() {
    // Calculate observed frequency using Doppler formula
    const numerator = dopplerParams.waveSpeed + dopplerParams.observerSpeed;
    const denominator = dopplerParams.waveSpeed - dopplerParams.sourceSpeed;
    const observedFrequency = dopplerParams.sourceFreq * (numerator / denominator);
    
    // Update displays
    observedFreq.textContent = `${observedFrequency.toFixed(1)} Hz`;
    const change = observedFrequency - dopplerParams.sourceFreq;
    const percentChange = (change / dopplerParams.sourceFreq) * 100;
    freqChange.textContent = `${change.toFixed(1)} Hz (${percentChange.toFixed(1)}%)`;
    
    // Update source and observer positions
    dopplerSource.style.left = `${dopplerParams.sourceX * 100}%`;
    dopplerObserver.style.left = `${dopplerParams.observerX * 100}%`;
    
    return observedFrequency;
}

// Draw Doppler waves
function drawDopplerWaves() {
    dopplerCtx.clearRect(0, 0, dopplerCanvas.width, dopplerCanvas.height);
    
    const centerY = dopplerCanvas.height / 2;
    const waveCount = 5; // Number of waves to show
    const waveLength = dopplerCanvas.width / waveCount;
    
    // Draw waves moving outward from source
    dopplerCtx.beginPath();
    for (let i = 0; i < dopplerCanvas.width; i++) {
        const x = i;
        // Calculate wave position based on source movement
        const wavePos = (i - dopplerParams.sourceX * dopplerCanvas.width) / waveLength;
        const y = centerY + 20 * Math.sin(wavePos * Math.PI * 2 + dopplerParams.wavePhase);
        
        if (i === 0) {
            dopplerCtx.moveTo(x, y);
        } else {
            dopplerCtx.lineTo(x, y);
        }
    }
    
    dopplerCtx.strokeStyle = '#9b59b6';
    dopplerCtx.lineWidth = 2;
    dopplerCtx.stroke();
    
    // Update phase for animation
    dopplerParams.wavePhase += 0.05;
    
    // Add waves to array for visualization
    if (frameCount % 10 === 0) {
        dopplerParams.waves.push({
            x: dopplerParams.sourceX * dopplerCanvas.width,
            radius: 1,
            alpha: 1
        });
    }
    
    // Draw expanding circles for wave fronts
    dopplerParams.waves.forEach((wave, index) => {
        wave.radius += 0.5;
        wave.alpha -= 0.01;
        
        dopplerCtx.beginPath();
        dopplerCtx.arc(wave.x, centerY, wave.radius, 0, Math.PI * 2);
        dopplerCtx.strokeStyle = `rgba(155, 89, 182, ${wave.alpha})`;
        dopplerCtx.lineWidth = 1;
        dopplerCtx.stroke();
        
        if (wave.alpha <= 0) {
            dopplerParams.waves.splice(index, 1);
        }
    });
}

// Animation loop for Doppler effect
let frameCount = 0;
function animateDoppler() {
    frameCount++;
    drawDopplerWaves();
    updateDopplerEffect();
    requestAnimationFrame(animateDoppler);
}

// Event listeners for Doppler controls
dopplerSourceSpeed.addEventListener('input', function() {
    dopplerParams.sourceSpeed = parseInt(this.value);
    dopplerParams.sourceX = 0.2 + (dopplerParams.sourceSpeed / 100) * 0.6;
    dopplerSourceSpeedValue.textContent = `${this.value} m/s`;
});

dopplerObserverSpeed.addEventListener('input', function() {
    dopplerParams.observerSpeed = parseInt(this.value);
    dopplerParams.observerX = 0.8 + (dopplerParams.observerSpeed / 50) * 0.1;
    dopplerObserverSpeedValue.textContent = `${this.value} m/s`;
});

dopplerWaveSpeed.addEventListener('input', function() {
    dopplerParams.waveSpeed = parseInt(this.value);
    dopplerWaveSpeedValue.textContent = `${this.value} m/s`;
});

dopplerSourceFreq.addEventListener('input', function() {
    dopplerParams.sourceFreq = parseInt(this.value);
    dopplerSourceFreqValue.textContent = `${this.value} Hz`;
});

// Initialize and start animation
window.addEventListener('load', function() {
    initDopplerCanvas();
    animateDoppler();
});

window.addEventListener('resize', function() {
    initDopplerCanvas();
});

    // Wave parameters
    let waveParams = {
        type: 'transverse',
        amplitude: parseInt(amplitudeSlider.value),
        frequency: parseFloat(frequencySlider.value),
        wavelength: parseInt(wavelengthSlider.value),
        phase: 0,
        // Added for longitudinal wave
        particleSpacing: 30,  // Base spacing between particles
        maxDisplacement: 20   // Maximum particle displacement
    };

    // Animation variables
    let animationId = null;
    let isAnimating = true;
    let isDragging = false;
    let dragStartX = 0;
    let dragStartY = 0;
    let manualWavePoints = [];

    // Initialize manual wave points
    function initManualWave() {
        manualWavePoints = [];
        const segments = 50;
        for (let i = 0; i <= segments; i++) {
            const x = (i / segments) * waveCanvas.width;
            manualWavePoints.push({
                x: x,
                y: waveCanvas.height / 2,
                vy: 0 // vertical velocity
            });
        }
    }
    const MEDIUM_SPEEDS = {
        solid: 1150.0,  // Fastest (e.g., seismic waves in rock)
        liquid: 1.5, // Medium (e.g., sound in water)
        gas: 1.0     // Slowest (e.g., sound in air)
    };

    // Update display values when sliders change
    amplitudeSlider.addEventListener('input', function() {
        waveParams.amplitude = parseInt(this.value);
        amplitudeValue.textContent = this.value;
    });

    frequencySlider.addEventListener('input', function() {
        waveParams.frequency = parseFloat(this.value);
        frequencyValue.textContent = this.value;
    });

    wavelengthSlider.addEventListener('input', function() {
        waveParams.wavelength = parseInt(this.value);
        wavelengthValue.textContent = this.value;
    });

    waveTypeSelect.addEventListener('change', function() {
        waveParams.type = this.value;
        manualWavePoints = []; // Reset manual wave when changing type
    });

    // Handle window resize
    window.addEventListener('resize', function() {
        waveCanvas.width = waveCanvas.parentElement.clientWidth;
        manualWavePoints = []; // Reset points on resize
    });

    // Dark mode toggle
    darkModeToggle.addEventListener('click', () => {
        document.body.classList.toggle('dark-mode');
        darkModeToggle.textContent = document.body.classList.contains('dark-mode') ? '☀️ Light Mode' : '🌓 Dark Mode';
    });

    // Start/stop animation when canvas is clicked
    waveCanvas.addEventListener('click', function() {
        if (isAnimating) {
            cancelAnimationFrame(animationId);
            isAnimating = false;
        } else {
            animateWave();
            isAnimating = true;
        }
    });

    // Calculate wave properties
    calculateBtn.addEventListener('click', calculateWaveProperties);

    // Mouse/touch event handlers for wave manipulation
    waveCanvas.addEventListener('mousedown', startDrag);
    waveCanvas.addEventListener('mousemove', dragWave);
    waveCanvas.addEventListener('mouseup', endDrag);
    waveCanvas.addEventListener('mouseleave', endDrag);
    solidBtn.addEventListener('click', () => setMedium('solid'));
    liquidBtn.addEventListener('click', () => setMedium('liquid'));
    gasBtn.addEventListener('click', () => setMedium('gas'));
    waveCanvas.addEventListener('touchstart', handleTouch);
    waveCanvas.addEventListener('touchmove', handleTouch);
    waveCanvas.addEventListener('touchend', endDrag);
    waveCanvas.addEventListener('dblclick', resetWaveDisplay);

    function handleTouch(e) {
        e.preventDefault();
        if (e.touches) {
            const touch = e.touches[0];
            const mouseEvent = new MouseEvent(
                e.type.replace('touch', 'mouse'),
                {
                    clientX: touch.clientX,
                    clientY: touch.clientY
                }
            );
            if (e.type === 'touchstart') {
                startDrag(mouseEvent);
            } else {
                dragWave(mouseEvent);
            }
        }
    }

    function setMedium(medium) {
    // Remove active class from all buttons first
    [solidBtn, liquidBtn, gasBtn].forEach(btn => {
        btn.classList.remove('active');
        btn.style.backgroundColor = ''; // Reset background
    });
    
    // Set active button with green color
    const activeBtn = document.getElementById(`${medium}Btn`);
    activeBtn.classList.add('active');
    activeBtn.style.backgroundColor = '#2ecc71'; // Green color
    
    // Set wave parameters based on medium
    let speed, waveType;
    switch(medium) {
        case 'solid':
            waveParams.frequency = 2.5;
            waveParams.wavelength = 180;
            speed = "5000-6000 m/s (Typical for seismic waves in rock)";
            waveType = "Transverse & Longitudinal";
            break;
        case 'liquid':
            waveParams.frequency = 1.8;
            waveParams.wavelength = 140;
            speed = "1500 m/s (Sound in water)";
            waveType = "Longitudinal";
            break;
        case 'gas':
            waveParams.frequency = 1.0;
            waveParams.wavelength = 100;
            speed = "343 m/s (Sound in air at 20°C)";
            waveType = "Longitudinal";
            break;
    }
    
    // Update display
    waveSpeedLabel.innerHTML = `
        <strong>${medium.toUpperCase()}</strong>: ${speed}<br>
        Wave Type: ${waveType}
    `;
    
    // Update sliders and values
    frequencySlider.value = waveParams.frequency;
    wavelengthSlider.value = waveParams.wavelength;
    frequencyValue.textContent = waveParams.frequency.toFixed(1);
    wavelengthValue.textContent = waveParams.wavelength;
    
    // Reset any manual interaction
    resetInteraction();
}

    function hideWaveLabels() {
    waveLabels.forEach(label => {
        label.style.opacity = '0';
        label.style.position = 'absolute';
        label.style.pointerEvents = '';
    });
}

    function showWaveLabels() {
    waveLabels.forEach(label => {
        label.style.opacity = '0';
        label.style.position = '';
        label.style.pointerEvents = '';
    });
}
    function updateCanvasLabels() {
    canvasLabels.innerHTML = `
        <div><strong>Type:</strong> ${waveParams.type === 'transverse' ? 'Transverse' : 'Longitudinal'}</div>
        <div><strong>Amplitude:</strong> ${waveParams.amplitude}</div>
        <div><strong>Frequency:</strong> ${waveParams.frequency.toFixed(1)} Hz</div>
        <div><strong>Wavelength:</strong> ${waveParams.wavelength}</div>
    `;
}
    function resetWaveDisplay() {
    showWaveLabels();
    manualWavePoints = [];
    isDragging = false;
    
    // Reset to default wave
    waveParams.amplitude = 20;
    waveParams.frequency = 1.0;
    waveParams.wavelength = 100;
    waveParams.phase = 0;
    waveParams.animationSpeed = 1.0;
    
    // Update sliders
    amplitudeSlider.value = waveParams.amplitude;
    frequencySlider.value = waveParams.frequency;
    wavelengthSlider.value = waveParams.wavelength;
    
    // Update displayed values
    amplitudeValue.textContent = waveParams.amplitude;
    frequencyValue.textContent = waveParams.frequency.toFixed(1);
    wavelengthValue.textContent = waveParams.wavelength;
    
    // Remove active state from medium buttons
}
    function startDrag(e) {
    waveParams.amplitude = 0;
    waveParams.frequency = 0;
    waveParams.wavelength = 0;
    
    // Update sliders and displayed values
    amplitudeSlider.value = 0;
    frequencySlider.value = 0;
    wavelengthSlider.value = 0;
    amplitudeValue.textContent = '0';
    frequencyValue.textContent = '0';
    wavelengthValue.textContent = '0';
        const rect = waveCanvas.getBoundingClientRect();
        dragStartX = e.clientX - rect.left;
        dragStartY = e.clientY - rect.top;
        isDragging = true;

        [solidBtn, liquidBtn, gasBtn].forEach(btn => {
        btn.classList.remove('active');
        btn.style.backgroundColor = '';
    });
        waveSpeedLabel.textContent = '';
        if (waveParams.type === 'transverse') {
            if (manualWavePoints.length === 0) initManualWave();
            
            let minDist = Infinity;
            let nearestIndex = -1;
            
            for (let i = 0; i < manualWavePoints.length; i++) {
                const point = manualWavePoints[i];
                const dist = Math.sqrt(Math.pow(point.x - dragStartX, 2) + Math.pow(point.y - dragStartY, 2));
                if (dist < minDist && dist < 30) {
                    minDist = dist;
                    nearestIndex = i;
                }
            }
            
            if (nearestIndex !== -1) {
                manualWavePoints[nearestIndex].y = dragStartY;
                manualWavePoints[nearestIndex].vy = (dragStartY - waveCanvas.height/2) * 0.5;
            }
        }
    }
    function resetInteraction() {
    // Show canvas labels
    canvasLabels.style.opacity = '1';
    updateCanvasLabels();
    
    // Reset manual wave points
    manualWavePoints = [];
    isDragging = false;
    
    // Ensure parameters aren't 0 (use defaults if needed)
    if (waveParams.amplitude === 0) {
        waveParams.amplitude = parseInt(amplitudeSlider.defaultValue) || 20;
        amplitudeSlider.value = waveParams.amplitude;
        amplitudeValue.textContent = waveParams.amplitude;
    }
    
    if (waveParams.frequency === 0) {
        waveParams.frequency = parseFloat(frequencySlider.defaultValue) || 1.0;
        frequencySlider.value = waveParams.frequency;
        frequencyValue.textContent = waveParams.frequency.toFixed(1);
    }
    
    if (waveParams.wavelength === 0) {
        waveParams.wavelength = parseInt(wavelengthSlider.defaultValue) || 100;
        wavelengthSlider.value = waveParams.wavelength;
        wavelengthValue.textContent = waveParams.wavelength;
    }
}
    function dragWave(e) {
        if (!isDragging) return;
        
        const rect = waveCanvas.getBoundingClientRect();
        const mouseX = e.clientX - rect.left;
        const mouseY = e.clientY - rect.top;
        
        if (waveParams.type === 'transverse' && manualWavePoints.length > 0) {
            let minDist = Infinity;
            let nearestIndex = -1;
            
            for (let i = 0; i < manualWavePoints.length; i++) {
                const point = manualWavePoints[i];
                const dist = Math.sqrt(Math.pow(point.x - mouseX, 2) + Math.pow(point.y - mouseY, 2));
                if (dist < minDist) {
                    minDist = dist;
                    nearestIndex = i;
                }
            }
            
            if (nearestIndex !== -1 && minDist < 50) {
                manualWavePoints[nearestIndex].y = mouseY;
                manualWavePoints[nearestIndex].vy = (mouseY - manualWavePoints[nearestIndex].y) * 0.3;
            }
        }
        
        dragStartX = mouseX;
        dragStartY = mouseY;
    }

    function endDrag() {
        isDragging = false;
    }

    // Update manual wave physics
    function updateManualWave() {
        if (waveParams.type !== 'transverse' || manualWavePoints.length === 0) return;
        // Simple wave propagation physics
        for (let i = 1; i < manualWavePoints.length - 1; i++) {
            const point = manualWavePoints[i];
            const left = manualWavePoints[i-1];
            const right = manualWavePoints[i+1];
            
            // Spring force from neighbors
            const springForce = 0.1 * ((left.y - point.y) + (right.y - point.y));
            
            // Damping
            const damping = -0.1 * point.vy;
            
            // Update velocity and position
            point.vy += springForce + damping;
            point.y += point.vy;
            
            // Gradual return to equilibrium
            point.vy += (waveCanvas.height/2 - point.y) * 0.01;
        }
        
        // Boundary conditions (fixed ends)
        manualWavePoints[0].y = waveCanvas.height/2;
        manualWavePoints[0].vy = 0;
        manualWavePoints[manualWavePoints.length-1].y = waveCanvas.height/2;
        manualWavePoints[manualWavePoints.length-1].vy = 0;
    }

    // Wave drawing functions
    function drawWave() {
        ctx.clearRect(0, 0, waveCanvas.width, waveCanvas.height);
        
        const centerY = waveCanvas.height / 2;
        const isDarkMode = document.body.classList.contains('dark-mode');
        
        if (waveParams.type === 'transverse') {
            if (manualWavePoints.length === 0) {
                // Draw standard transverse wave if not manually interacting
                const points = [];
                const segments = 200;
                ctx.beginPath();
                
                for (let i = 0; i <= segments; i++) {
                    const x = (i / segments) * waveCanvas.width;
                    const xInWavelengths = (x / waveCanvas.width) * (waveCanvas.width / waveParams.wavelength * 2);
                    const y = centerY + waveParams.amplitude * Math.sin(xInWavelengths * Math.PI + waveParams.phase);
                    
                    if (i === 0) {
                        ctx.moveTo(x, y);
                    } else {
                        ctx.lineTo(x, y);
                    }
                    
                    points.push({x, y});
                }
                
                ctx.strokeStyle = '#3498db';
                ctx.lineWidth = 2;
                ctx.stroke();
                
                // Draw particles (for visualization)
                for (let i = 0; i < points.length; i += 10) {
                    const point = points[i];
                    ctx.beginPath();
                    ctx.arc(point.x, point.y, 3, 0, Math.PI * 2);
                    ctx.fillStyle = '#e74c3c';
                    ctx.fill();
                    
                    // Draw equilibrium position indicator
                    ctx.beginPath();
                    ctx.moveTo(point.x, centerY);
                    ctx.lineTo(point.x, point.y);
                    ctx.strokeStyle = 'rgba(0, 0, 0, 0.2)';
                    ctx.lineWidth = 1;
                    ctx.stroke();
                }
            } else {
                // Draw manual wave
                updateManualWave();
                
                ctx.beginPath();
                ctx.moveTo(manualWavePoints[0].x, manualWavePoints[0].y);
                
                for (let i = 1; i < manualWavePoints.length; i++) {
                    const point = manualWavePoints[i];
                    ctx.lineTo(point.x, point.y);
                }
                
                ctx.strokeStyle = '#3498db';
                ctx.lineWidth = 2;
                ctx.stroke();
                
                // Draw particles
                for (let i = 0; i < manualWavePoints.length; i += 2) {
                    const point = manualWavePoints[i];
                    ctx.beginPath();
                    ctx.arc(point.x, point.y, 3, 0, Math.PI * 2);
                    ctx.fillStyle = '#e74c3c';
                    ctx.fill();
                    
                    // Draw equilibrium position
                    ctx.beginPath();
                    ctx.moveTo(point.x, centerY);
                    ctx.lineTo(point.x, point.y);
                    ctx.strokeStyle = 'rgba(0, 0, 0, 0.2)';
                    ctx.lineWidth = 1;
                    ctx.stroke();
                }
            }
            
            // Draw equilibrium line
            ctx.beginPath();
            ctx.moveTo(0, centerY);
            ctx.lineTo(waveCanvas.width, centerY);
            ctx.strokeStyle = 'rgba(0, 0, 0, 0.1)';
            ctx.lineWidth = 1;
            ctx.stroke();
        } else {
            // Draw longitudinal wave
            const particleCount = Math.min(40, Math.floor(waveCanvas.width / waveParams.particleSpacing));
            const spacing = waveCanvas.width / particleCount;
            //const compressionWidth = waveParams.wavelength / 4;
            waveParams.phase += 0.1 * waveParams.frequency;
            
            for (let i = 0; i < particleCount; i++) {
                const x = i * spacing + spacing/2;
                
                // Draw equilibrium position marker
                ctx.beginPath();
                ctx.arc(x, centerY, 2, 0, Math.PI * 2);
                ctx.fillStyle = isDarkMode ? 'rgba(255,255,255,0.3)' : 'rgba(0, 0, 0, 0.3)';
                ctx.fill();
            }

            // Draw particles and their movement
            for (let i = 0; i < particleCount; i++) {
                const x = i * spacing + spacing/2;
                const xInWave = (x / waveCanvas.width) * (waveCanvas.width / waveParams.wavelength * 2 * Math.PI) + waveParams.phase;
                const displacement = waveParams.maxDisplacement * Math.sin(xInWave);
                
                // Draw displaced particle
                ctx.beginPath();
                ctx.arc(x + displacement, centerY, 5, 0, Math.PI * 2);
                ctx.fillStyle = '#e74c3c';
                ctx.fill();
                
                // Draw connection line between equilibrium and displaced position
                ctx.beginPath();
                ctx.moveTo(x, centerY);
                ctx.lineTo(x + displacement, centerY);
                ctx.strokeStyle = isDarkMode ? 'rgba(255,255,255,0.2)' : 'rgba(0, 0, 0, 0.2)';
                ctx.lineWidth = 1;
                ctx.stroke();
                
                // Label compressions and rarefactions
                if (i % 5 === 0) {
                    const isCompression = Math.abs(displacement) > waveParams.maxDisplacement * 0.7;
                    ctx.fillStyle = isCompression ? 'rgba(46, 204, 113, 0.3)' : 'rgba(52, 152, 219, 0.3)';
                    const labelWidth = spacing * 4;
                    ctx.fillRect(x - labelWidth/2, centerY - 40, labelWidth, 20);
                    
                    ctx.fillStyle = isDarkMode ? '#ffffff' : '#2c3e50';
                    ctx.textAlign = 'center';
                    ctx.font = 'bold 12px Arial';
                    ctx.fillText(isCompression ? 'COMPRESSION' : 'RAREFACTION', x, centerY - 25);
                }
            }
            
            // Draw particle motion indicators
            for (let i = 2; i < particleCount - 2; i += 3) {
                const x = i * spacing + spacing/2;
                const xInWave = (x / waveCanvas.width) * (waveCanvas.width / waveParams.wavelength * 2 * Math.PI) + waveParams.phase;
                const motionDirection = Math.cos(xInWave) > 0 ? '→' : '←';
                
                ctx.fillStyle = isDarkMode ? 'rgba(255,255,255,0.7)' : 'rgba(0,0,0,0.7)';
                ctx.textAlign = 'center';
                ctx.font = 'bold 16px Arial';
                ctx.fillText(motionDirection, x, centerY + 25);
            }
            
            // Draw wave direction indicator
            ctx.fillStyle = isDarkMode ? '#ffffff' : '#2c3e50';
            ctx.textAlign = 'right';
            ctx.font = 'bold 14px Arial';
            ctx.fillText('Wave Direction →', waveCanvas.width - 10, centerY + 50);
        }
    }

    function animateWave() {
        if (!isDragging) {
        updateCanvasLabels();
    }
        if (waveParams.type === 'transverse' && manualWavePoints.length === 0) {
            waveParams.phase += 0.05 * waveParams.frequency;
        }
        drawWave();
        animationId = requestAnimationFrame(animateWave);
    }

    // Calculate wave properties
    function calculateWaveProperties() {
        const wavelength = parseFloat(calcWavelength.value);
        const frequency = parseFloat(calcFrequency.value);
        const amplitude = parseFloat(calcAmplitude.value);
        
        if (isNaN(wavelength) || isNaN(frequency) || isNaN(amplitude)) {
            resultsContainer.innerHTML = '<p class="error">Please enter valid numbers for all fields</p>';
            return;
        }
        
        if (frequency <= 0 || wavelength <= 0) {
            resultsContainer.innerHTML = '<p class="error">Frequency and wavelength must be greater than zero</p>';
            return;
        }
        
        // Calculate locally for immediate feedback
        const waveSpeed = wavelength * frequency;
        const period = 1 / frequency;
        const angularFrequency = 2 * Math.PI * frequency;
        const waveNumber = 2 * Math.PI / wavelength;
        
        resultsContainer.innerHTML = `
            <div class="result-item">
                <span class="result-label">Wave Speed (v = λf):</span>
                <span class="result-value">${waveSpeed.toFixed(2)} m/s</span>
            </div>
            <div class="result-item">
                <span class="result-label">Period (T = 1/f):</span>
                <span class="result-value">${period.toFixed(4)} s</span>
            </div>
            <div class="result-item">
                <span class="result-label">Angular Frequency (ω = 2πf):</span>
                <span class="result-value">${angularFrequency.toFixed(2)} rad/s</span>
            </div>
            <div class="result-item">
                <span class="result-label">Wave Number (k = 2π/λ):</span>
                <span class="result-value">${waveNumber.toFixed(4)} rad/m</span>
            </div>
            <div class="wave-equation">
                <p>The wave equation for these parameters:</p>
                <p class="equation">y(x,t) = ${amplitude.toFixed(2)} sin(${waveNumber.toFixed(2)}x - ${angularFrequency.toFixed(2)}t)</p>
            </div>
        `;
        
        // Update visualization to match calculation
        waveParams.amplitude = amplitude * 100; // Scale for visualization
        waveParams.frequency = frequency;
        waveParams.wavelength = wavelength * 100; // Scale for visualization
        amplitudeSlider.value = waveParams.amplitude;
        frequencySlider.value = waveParams.frequency;
        wavelengthSlider.value = waveParams.wavelength;
        amplitudeValue.textContent = waveParams.amplitude;
        frequencyValue.textContent = waveParams.frequency;
        wavelengthValue.textContent = waveParams.wavelength;

        [solidBtn, liquidBtn, gasBtn].forEach(btn => {
        btn.classList.remove('active');
        btn.style.backgroundColor = '';
    });
    waveSpeedLabel.textContent = '';
    }

    document.addEventListener('DOMContentLoaded', function() {
    updateCanvasLabels();
    
    // Set default
});

waveTypeSelect.addEventListener('change', function() {
    waveParams.type = this.value;
    manualWavePoints = [];
    
    // Show labels when switching to longitudinal
    if (this.value === 'longitudinal') {
        resetInteraction();
    }
    
    // Reset medium button colors
    [solidBtn, liquidBtn, gasBtn].forEach(btn => {
        btn.style.backgroundColor = '';
    });
});

    // Application frequency visualization
    document.querySelectorAll('.application-card').forEach(card => {
    card.addEventListener('click', function() {
        // First reset any interaction state
        resetInteraction();
        
        const freqDisplay = this.querySelector('.frequency-display');
        const frequency = parseFloat(freqDisplay.dataset.freq);
        
        // Scale frequency for visualization
        let visFrequency;
        if (frequency > 1000) {
            visFrequency = frequency / 10000; // Scale down ultrasound frequencies
        } else if (frequency < 1) {
            visFrequency = frequency * 10; // Scale up seismic frequencies
        } else {
            visFrequency = frequency / 10;
        }
        
        // Set wave parameters (don't set to 0)
        waveParams.amplitude = this.querySelector('h4').textContent.includes('Musical') ? 30 : 15;
        waveParams.frequency = visFrequency;
        waveParams.wavelength = this.querySelector('h4').textContent.includes('Musical') ? 100 : 150;
        
        // Update sliders and display
        amplitudeSlider.value = waveParams.amplitude;
        frequencySlider.value = waveParams.frequency;
        wavelengthSlider.value = waveParams.wavelength;
        amplitudeValue.textContent = waveParams.amplitude;
        frequencyValue.textContent = waveParams.frequency.toFixed(2);
        wavelengthValue.textContent = waveParams.wavelength;
        
        // For musical instruments, show standing wave pattern
        if (this.querySelector('h4').textContent.includes('Musical')) {
            waveParams.type = 'transverse';
            waveTypeSelect.value = 'transverse';
        }
        
        // For ultrasound/sonar, show high frequency
        if (frequency > 10000) {
            waveParams.amplitude = 10;
            amplitudeSlider.value = 10;
            amplitudeValue.textContent = '10';
        }
        
        // Update canvas labels
        updateCanvasLabels();
        
        // Reset medium buttons
        [solidBtn, liquidBtn, gasBtn].forEach(btn => {
            btn.classList.remove('active');
            btn.style.backgroundColor = '';
        });
    });
});

    // Start animation
    animateWave();
});