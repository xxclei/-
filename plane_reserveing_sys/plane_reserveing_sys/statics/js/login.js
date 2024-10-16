particlesJS("particle-container", {
    particles: {
        number: {
            value: 150,
            density: {
                enable: true,
                value_area: 800
            }
        },
        color: {
            value: '#6ab3f7'
        },
        shape: {
            type: 'circle',
            stroke: {
                width: 0,
                color: '#000000'
            },
            polygon: {
                nb_sides: 5
            },
            image: {
                src: 'img/github.svg',
                width: 100,
                height: 100
            }
        },
        opacity: {
            value: 0.5,
            random: false,
            anim: {
                enable: false,
                speed: 1,
                opacity_min: 0.1,
                sync: false
            }
        },
        size: {
            value: 3,
            random: true,
            anim: {
                enable: false,
                speed: 40,
                size_min: 0.1,
                sync: false
            }
        },
        line_linked: {
            enable: true,
            distance: 150,
            color: '#6ab3f7',
            opacity: 0.6,
            width: 1
        },
        anim: {
            enable: true,
            speed: 2
        }
    },
    interactivity: {
        detect_on: 'canvas',
        events: {
            onhover: {
                enable: true,
                mode: 'line'
            },
            onclick: {
                enable: true,
                mode: 'repulse'
            },
            resize: true
        },
        modes: {
            line: {
                type: 'line',
                speed: 3,
                straight: false,
                line_linked: {
                    enable: true,
                    distance: 200
                }
            },
            repulse: {
                distance: 200,
                duration: 0.4
            }
        }
    },
    retina_detect: true
});