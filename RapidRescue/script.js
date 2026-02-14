// Data for functionality
const hospitals = [
    { name: "City General Hospital", type: "General", distance: "1.2 km", time: "5 mins", image: "https://t4.ftcdn.net/jpg/02/11/15/48/360_F_211154804_w5Jd3s83r3l1yf1c.jpg" },
    { name: "Apollo Emergency Care", type: "Specialized", distance: "2.5 km", time: "12 mins", image: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR_uK7x9x7d8z3y_8q9g_9_5z_x_6_7_8_9_0&usqp=CAU" },
    { name: "LifeLine Trauma Center", type: "Trauma", distance: "3.8 km", time: "18 mins", image: "https://cdn.iconscout.com/icon/free/png-256/free-hospital-building-icon-download-in-svg-png-gif-file-formats--medical-health-healthcare-clinic-buildings-vol-3-pack-city-architecture-icons-4235310.png?f=webp" },
    { name: "Green Valley Clinic", type: "Clinic", distance: "4.5 km", time: "22 mins", image: "https://ui-avatars.com/api/?name=Clinic&background=random" },
    { name: "St. John's Medical", type: "General", distance: "6.0 km", time: "30 mins", image: "https://ui-avatars.com/api/?name=Hospital&background=random" }
];

const helpers = [
    { name: "Rahul S.", role: "Volunteer", distance: "400m", rating: "4.8", image: "https://ui-avatars.com/api/?name=Rahul+S&background=random" },
    { name: "Priya M.", role: "Nurse", distance: "800m", rating: "5.0", image: "https://ui-avatars.com/api/?name=Priya+M&background=random" },
    { name: "Vijay K.", role: "Driver", distance: "1.1km", rating: "4.7", image: "https://ui-avatars.com/api/?name=Vijay+K&background=random" },
    { name: "Amit B.", role: "Paramedic", distance: "1.5km", rating: "4.9", image: "https://ui-avatars.com/api/?name=Amit+B&background=random" }
];

// Navigation Logic
function navigateTo(screenId) {
    // Hide all screens
    const screens = document.querySelectorAll('.screen');
    screens.forEach(s => s.classList.remove('active'));

    // Show target screen
    const target = document.getElementById(screenId);
    if (target) {
        target.classList.add('active');
        window.scrollTo(0, 0);
    }

    // Populate data if needed
    if (screenId === 'hospital-screen') loadHospitals();
    if (screenId === 'help-screen') loadHelpers();

    // Update Top Nav
    updateTopNav(screenId);
}

function updateTopNav(screenId) {
    const navLinks = document.querySelectorAll('.nav-links a');
    navLinks.forEach(link => link.classList.remove('active'));

    // Mapping screen IDs to Nav IDs
    const map = {
        'home-screen': 'nav-home',
        'hospital-screen': 'nav-hospitals',
        'help-screen': 'nav-help',
        'tracking-screen': 'nav-track'
    };

    if (map[screenId]) {
        const activeLink = document.getElementById(map[screenId]);
        if (activeLink) activeLink.classList.add('active');
    }
}

// Emergency Activation Logic
function activateEmergency(type = 'general') {
    const sosBtn = document.getElementById('sos-btn');

    // Animation feedback
    sosBtn.style.transform = 'scale(0.9)';
    setTimeout(() => {
        sosBtn.style.transform = 'scale(1)';
        navigateTo('emergency-screen');

        // Simulate "Contacting..." delay then switch to tracking
        setTimeout(() => {
            // alert("Ambulance Dispatched! Switching to Live Tracking."); // Removed alert for smoother flow
            navigateTo('tracking-screen');
        }, 3000);

    }, 200);
}

// Data Loading Functions (Updated card styles for Grid)
function loadHospitals() {
    const listInfo = document.getElementById('hospitals-list');
    listInfo.innerHTML = ''; // Clear previous

    hospitals.forEach(hospital => {
        const card = `
            <div class="list-card" onclick="navigateTo('tracking-screen')">
                 <div style="width: 60px; height: 60px; background: #e3f2fd; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; color: #2962FF;">
                    <i class="fas fa-hospital-alt"></i>
                </div>
                <div class="card-info" style="flex:1">
                    <h3>${hospital.name}</h3>
                    <p style="color: #666">${hospital.type}</p>
                    <div style="margin-top: 5px; display: flex; gap: 10px; font-size: 0.85rem; color: #888;">
                         <span><i class="fas fa-map-marker-alt"></i> ${hospital.distance}</span>
                         <span style="color: #00C853; font-weight:600"><i class="fas fa-bolt"></i> ${hospital.time}</span>
                    </div>
                </div>
                <i class="fas fa-chevron-right" style="color: #ccc"></i>
            </div>
        `;
        listInfo.innerHTML += card;
    });
}

function loadHelpers() {
    const listInfo = document.getElementById('helpers-list');
    listInfo.innerHTML = '';

    helpers.forEach(helper => {
        const card = `
            <div class="list-card" onclick="navigateTo('tracking-screen')">
                <img src="${helper.image}" alt="Helper">
                <div class="card-info" style="flex:1">
                    <h3>${helper.name}</h3>
                    <p style="color: #666">${helper.role}</p>
                    <div style="margin-top: 5px; font-size: 0.85rem; color: #888;">
                         <span><i class="fas fa-map-marker-alt"></i> ${helper.distance} away</span>
                    </div>
                </div>
                 <div class="distance-badge" style="background: #e8f5e9; color: #2e7d32;">${helper.rating} <i class="fas fa-star" style="font-size:0.6rem"></i></div>
            </div>
        `;
        listInfo.innerHTML += card;
    });
}


// Initialize
document.addEventListener('DOMContentLoaded', () => {
    // Any init logic
    console.log("RapidRescue Prototype Loaded");
});
