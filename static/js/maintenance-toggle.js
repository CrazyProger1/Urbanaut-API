document.addEventListener('DOMContentLoaded', function() {
    // Create toggle HTML
    const toggleHTML = `
        <style>
        .maintenance-toggle {
            position: fixed;
            top: 15px;
            right: 200px;
            z-index: 1000;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .toggle-switch {
            position: relative;
            width: 50px;
            height: 26px;
            background-color: #ccc;
            border-radius: 13px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        .toggle-switch.active {
            background-color: #4caf50;
        }
        .toggle-slider {
            position: absolute;
            top: 3px;
            left: 3px;
            width: 20px;
            height: 20px;
            background-color: white;
            border-radius: 50%;
            transition: left 0.3s;
        }
        .toggle-switch.active .toggle-slider {
            left: 27px;
        }
        .toggle-label {
            font-size: 12px;
            color: #666;
        }
        </style>
        <div class="maintenance-toggle">
            <span class="toggle-label">Maintenance</span>
            <div class="toggle-switch" id="maintenanceToggle">
                <div class="toggle-slider"></div>
            </div>
        </div>
    `;

    // Find header and append toggle
    const header = document.querySelector('header') || document.querySelector('[role="banner"]') || document.body;
    const wrapper = document.createElement('div');
    wrapper.innerHTML = toggleHTML;
    header.appendChild(wrapper.firstElementChild);

    // Add click handler
    const toggle = document.getElementById('maintenanceToggle');
    if (toggle) {
        toggle.addEventListener('click', function() {
            fetch('/admin/maintenance/', { method: 'POST' })
                .then(() => window.location.reload())
                .catch(err => console.error('Error:', err));
        });
    }
});