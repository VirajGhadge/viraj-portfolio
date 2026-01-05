// ============================================
// VIRAJ GHADGE PORTFOLIO - JAVASCRIPT
// Smooth interactions and dynamic features
// ============================================

document.addEventListener('DOMContentLoaded', function() {
    // Navbar highlighting based on current page
    updateActiveNavLink();
    
    // Smooth scroll for internal links
    enableSmoothScroll();
    
    // Add animation to elements on scroll
    addScrollAnimations();
});

// ============================================
// Update Active Navigation Link
// ============================================

function updateActiveNavLink() {
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('.nav-link');
    
    navLinks.forEach(link => {
        const href = link.getAttribute('href');
        
        if ((currentPath === '/' && href === '/') || 
            (currentPath !== '/' && href === currentPath)) {
            link.style.color = '#e94b3c';
            link.style.fontWeight = '600';
        } else {
            link.style.color = '';
            link.style.fontWeight = '';
        }
    });
}

// ============================================
// Smooth Scroll for Internal Links
// ============================================

function enableSmoothScroll() {
    const links = document.querySelectorAll('a[href^="#"]');
    
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);
            
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

// ============================================
// Scroll Animations
// ============================================

function addScrollAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -100px 0px'
    };
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);
    
    // Observe all cards and sections
    const elementsToObserve = document.querySelectorAll(
        '.project-card, .education-card, .skill-category, .featured-card, .blog-post'
    );
    
    elementsToObserve.forEach(element => {
        element.style.opacity = '0';
        element.style.transform = 'translateY(20px)';
        element.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(element);
    });
}

// ============================================
// Typing Animation (Optional Enhancement)
// ============================================

function typeEffect(element, text, speed = 50) {
    let index = 0;
    element.textContent = '';
    
    function type() {
        if (index < text.length) {
            element.textContent += text.charAt(index);
            index++;
            setTimeout(type, speed);
        }
    }
    
    type();
}

// Add hover effects to buttons
document.addEventListener('DOMContentLoaded', function() {
    const buttons = document.querySelectorAll('.btn');
    
    buttons.forEach(button => {
        button.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-3px)';
        });
        
        button.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });
});

// ============================================
// Mobile Menu Toggle (For future expansion)
// ============================================

// You can add hamburger menu functionality here when needed

console.log('✨ Viraj Ghadge Portfolio - Ready!');
