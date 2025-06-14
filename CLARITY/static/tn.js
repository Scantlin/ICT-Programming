document.addEventListener('DOMContentLoaded', function() {
    console.log("Script loaded!"); // Debug check
    
    const clarity = document.getElementById('clarity');
    const production = document.getElementById('production');
    const lightRays = document.querySelector('.light-rays');
    const particlesContainer = document.querySelector('.particles');
    const glow = document.querySelector('.glow');

    // Debug elements
    console.log("Elements:", {
        clarity, 
        production,
        lightRays,
        particlesContainer,
        glow
    });

    function createParticles() {
        particlesContainer.innerHTML = '';
        
        for (let i = 0; i < 100; i++) {
            const particle = document.createElement('div');
            particle.classList.add('particle');
            
            // Random position and movement
            const x = Math.random() * 100;
            const y = Math.random() * 100;
            const tx = (Math.random() - 0.5) * 300;
            const ty = (Math.random() - 0.5) * 300;
            
            particle.style.left = `${x}%`;
            particle.style.top = `${y}%`;
            particle.style.setProperty('--tx', `${tx}px`);
            particle.style.setProperty('--ty', `${ty}px`);
            particle.style.animationDelay = `${Math.random() * 2}s`;
            
            particlesContainer.appendChild(particle);
        }
    }

    function playAnimation() {
        console.log("Starting animation..."); // Debug
        
        // Initial light effect
        setTimeout(() => {
            lightRays.style.opacity = 1;
            glow.style.opacity = 0.7;
            console.log("Light effects activated"); // Debug

            // Animate CLARITY
            setTimeout(() => {
                clarity.style.opacity = 1;
                clarity.style.transform = 'translateY(0)';
                console.log("CLARITY animated"); // Debug

                // Animate PRODUCTION
                setTimeout(() => {
                    production.style.opacity = 1;
                    production.style.transform = 'translateY(0)';
                    console.log("PRODUCTION animated"); // Debug

                    // Add particles
                    createParticles();
                    console.log("Particles created"); // Debug

                }, 800);
            }, 1500);
        }, 500);
    }

    playAnimation();
});