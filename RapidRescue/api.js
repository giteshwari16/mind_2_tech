// API Configuration
const API_BASE_URL = 'http://localhost:8000/api';

// API Helper Functions
class API {
    static async request(endpoint, options = {}) {
        const url = `${API_BASE_URL}${endpoint}`;
        const config = {
            headers: {
                'Content-Type': 'application/json',
                ...options.headers,
            },
            ...options,
        };

        try {
            const response = await fetch(url, config);
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return await response.json();
        } catch (error) {
            console.error('API Error:', error);
            throw error;
        }
    }

    // Emergency API
    static async createEmergencyRequest(data) {
        return this.request('/emergency/emergency-requests/', {
            method: 'POST',
            body: JSON.stringify(data),
        });
    }

    static async getNearbyEmergencies(lat, lng, radius = 10) {
        return this.request(`/emergency/emergency-requests/nearby/?lat=${lat}&lng=${lng}&radius=${radius}`);
    }

    static async acceptEmergencyRequest(id) {
        return this.request(`/emergency/emergency-requests/${id}/accept/`, {
            method: 'POST',
        });
    }

    static async resolveEmergencyRequest(id) {
        return this.request(`/emergency/emergency-requests/${id}/resolve/`, {
            method: 'POST',
        });
    }

    // Hospitals API
    static async getHospitals() {
        return this.request('/hospitals/hospitals/');
    }

    static async getNearbyHospitals(lat, lng, radius = 10) {
        return this.request(`/hospitals/hospitals/nearby/?lat=${lat}&lng=${lng}&radius=${radius}`);
    }

    static async getHospitalDetails(id) {
        return this.request(`/hospitals/hospitals/${id}/`);
    }

    static async getHospitalDepartments(id) {
        return this.request(`/hospitals/hospitals/${id}/departments/`);
    }

    static async addHospitalReview(id, reviewData) {
        return this.request(`/hospitals/hospitals/${id}/add_review/`, {
            method: 'POST',
            body: JSON.stringify(reviewData),
        });
    }

    static async getHospitalReviews(id) {
        return this.request(`/hospitals/hospitals/${id}/reviews/`);
    }
}

// Location Services
class LocationService {
    static async getCurrentPosition() {
        return new Promise((resolve, reject) => {
            if (!navigator.geolocation) {
                reject(new Error('Geolocation is not supported by this browser.'));
                return;
            }

            navigator.geolocation.getCurrentPosition(
                (position) => {
                    resolve({
                        latitude: position.coords.latitude,
                        longitude: position.coords.longitude,
                    });
                },
                (error) => {
                    reject(error);
                },
                {
                    enableHighAccuracy: true,
                    timeout: 10000,
                    maximumAge: 600000,
                }
            );
        });
    }

    static async getAddressFromCoords(lat, lng) {
        // In a real app, you'd use a geocoding service like Google Maps API
        // For now, return a formatted string
        return `Lat: ${lat.toFixed(6)}, Lng: ${lng.toFixed(6)}`;
    }
}

// Emergency Service Integration
class EmergencyService {
    static async activateEmergency(emergencyType, description, contactPhone) {
        try {
            // Get current location
            const location = await LocationService.getCurrentPosition();
            const address = await LocationService.getAddressFromCoords(location.latitude, location.longitude);

            // Create emergency request
            const emergencyData = {
                emergency_type: emergencyType,
                description: description,
                latitude: location.latitude,
                longitude: location.longitude,
                address: address,
                contact_phone: contactPhone,
            };

            const response = await API.createEmergencyRequest(emergencyData);
            return response;
        } catch (error) {
            console.error('Emergency activation failed:', error);
            throw error;
        }
    }
}

// Hospital Service Integration
class HospitalService {
    static async loadNearbyHospitals() {
        try {
            const location = await LocationService.getCurrentPosition();
            const hospitals = await API.getNearbyHospitals(location.latitude, location.longitude);
            return hospitals;
        } catch (error) {
            console.error('Failed to load nearby hospitals:', error);
            // Fallback to static data if API fails
            return [
                { name: "City General Hospital", hospital_type: "general", distance: "1.2 km", phone: "555-0101" },
                { name: "Apollo Emergency Care", hospital_type: "specialty", distance: "2.5 km", phone: "555-0102" },
            ];
        }
    }

    static async loadHospitalDetails(hospitalId) {
        try {
            const [hospital, departments, reviews] = await Promise.all([
                API.getHospitalDetails(hospitalId),
                API.getHospitalDepartments(hospitalId),
                API.getHospitalReviews(hospitalId),
            ]);

            return {
                ...hospital,
                departments,
                reviews,
            };
        } catch (error) {
            console.error('Failed to load hospital details:', error);
            throw error;
        }
    }
}
