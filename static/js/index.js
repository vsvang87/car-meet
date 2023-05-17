
const tl = gsap.timeline({defaults: {Easings: Expo.EaseOut}})

tl.from(".home-page", { scale: 0.6, duration: 2, opacity: 0, ease: Expo.EaseOut, delay: 0.2 }).to(".font-family", { clipPath: "polygon(0 0, 100% 0, 100% 100%, 0 100%)", y: 0, stagger: 0.3, duration: 1 }, "-=2.9")
  .to(".font-family", { clipPath: "polygon(0 0, 100% 0, 100% 0%, 0 0%)", y: -200, stagger: 0.3, duration: .3, delay: .5 })
  .to(".font-family", { clipPath: "polygon(0 0, 100% 0, 100% 100%, 0 100%)", y: 0, stagger: 0.3, duration: .3, delay: .5 })
  .to(".btn", { clipPath: "polygon(0 0, 100% 0, 100% 100%, 0 100%)", y:0 })
  .to(".local", {clipPath: "polygon(0 0, 100% 0, 100% 100%, 0 100%)", y:0, stagger: 0.3, opacity: 1, duration: 1}, "-=1.4")

