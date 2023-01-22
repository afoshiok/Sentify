/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
  "./index.html",
  "./src/**/*.{vue,js,ts,jsx,tsx}",
],
  theme: {
    extend: {},
  },
  plugins: [require("daisyui")],

  daisyui: {
    styled: true,
    themes: [
      {
        mytheme: {
        
              "primary": "#000000",
                      
              "secondary": "#e58124",
                      
              "accent": "#e5918e",
                      
              "neutral": "#201523",
                      
              "base-100": "#F1F3F8",
                      
              "info": "#6EB0F7",
                      
              "success": "#1AD59D",
                      
              "warning": "#EEC658",
                      
              "error": "#FB3613",
        },
      },
    ],
    base: false,
    utils: true,
    logs: true,
    rtl: false,
    prefix: "",
    darkTheme: "dark",
  },
}
