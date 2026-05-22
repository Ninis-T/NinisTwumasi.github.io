<!-- 
==================================================================
NINIS TWUMASI - COMPUTER SCIENCE ESSENTIALS FINAL PORTFOLIO
==================================================================
This is a single-file, fully responsive academic website.
It includes all CSS styling (via Tailwind), icons, layout structures, 
multi-page navigation routing, and interactive CS algorithms in one file.
Perfect for instant hosting on GitHub Pages!
==================================================================
-->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Website title shown in browser tab -->
    <title>Ninis Twumasi | Elegant CSE Portfolio</title>
    
    <!-- 
      PROCESS: TAILWIND CSS & STYLE CONFIGURATION
      We import Tailwind CSS to build a beautiful design without writing heavy external CSS.
      Below, we configure custom 'gold' and 'apple' colors to match your elegant gold-and-white theme.
    -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    colors: {
                        gold: {
                            50: '#FDFBF7',   // Creamy background white
                            100: '#F9F6EE',  // Soft alabaster sand
                            200: '#F3E9CE',  // Champagne gold accent
                            300: '#EADAA9',  // Warm gold highlights
                            500: '#D4AF37',  // Premium metallic gold leaf
                            600: '#C5A028',  // Burnished satin gold
                            700: '#A3801A',  // Classic antique gold
                            900: '#4E3E12',  // Deep gold bronze
                            950: '#2A2105',  // Dark golden obsidian
                        },
                        apple: {
                            gray: '#F5F5F7', // Apple standard light-gray
                            dark: '#08080A', // Premium dark mode background
                            zinc: '#121215', // Sleek cards for dark mode
                        }
                    },
                    fontFamily: {
                        mono: ['Fira Code', 'Courier New', 'monospace'],
                        sans: ['SF Pro Display', '-apple-system', 'BlinkMacSystemFont', 'Inter', 'sans-serif'],
                        serif: ['Playfair Display', 'Georgia', 'serif'],
                    }
                }
            }
        }
    </script>

    <!-- FontAwesome: Used to render high-quality professional vector icons throughout the site -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <!-- Google Fonts: We import Inter (sans-serif) for body text and Playfair Display (serif) for titles -->
    <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;600&family=Inter:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&display=swap" rel="stylesheet">

    <!-- 
      PROCESS: CUSTOM TRANSITIONS AND SCROLLBARS
      We write a tiny embedded CSS block for fluid animations when shuffling backgrounds,
      and custom golden scrollbars that match the Apple aesthetic.
    -->
    <style>
        html {
            scroll-behavior: smooth;
        }
        /* Smooth transitions for shuffling the hero section backgrounds */
        .bg-transition {
            transition: background-image 1.5s ease-in-out, background-color 0.5s;
        }
        /* Custom golden scrollbar on desktop viewports */
        ::-webkit-scrollbar {
            width: 8px;
            height: 8px;
        }
        ::-webkit-scrollbar-track {
            background: #FAF8F2;
        }
        .dark ::-webkit-scrollbar-track {
            background: #08080A;
        }
        ::-webkit-scrollbar-thumb {
            background: #D4AF37;
            border-radius: 10px;
        }
        /* Soft, luxury ambient glow borders */
        .gold-glow {
            box-shadow: 0 0 15px rgba(212, 175, 55, 0.1);
        }
        .gold-glow:hover {
            box-shadow: 0 0 25px rgba(212, 175, 55, 0.25);
        }
    </style>
</head>
<body class="bg-gold-50 text-gray-900 dark:bg-apple-dark dark:text-gray-100 font-sans transition-colors duration-300 min-h-screen flex flex-col overflow-x-hidden">

    <!-- 
      PROCESS: TOP UTILITY LIVE CUSTOMIZER BANNER
      This bar stays fixed at the top to let teachers or classmates know that they can 
      live-edit your variables (name, school, classes) right in the web browser!
    -->
    <div class="bg-gold-950 text-gold-100 text-xs py-2.5 px-4 flex justify-between items-center z-50 sticky top-0 border-b border-gold-700/30">
        <div class="flex items-center gap-2">
            <span class="bg-gold-500 text-apple-dark text-[10px] font-bold px-2 py-0.5 rounded tracking-wide">LIVE EDITOR</span>
            <span>Customize your details live! Perfect for demonstrating school-appropriate variables.</span>
        </div>
        <button onclick="toggleCustomizer()" class="underline hover:text-white font-medium transition text-[11px] flex items-center gap-1">
            <i class="fa-solid fa-sliders mr-1"></i> Toggle Panel
        </button>
    </div>

    <div class="flex flex-1 relative">
        <!-- 
          PROCESS: THE LIVE CUSTOMIZER SIDEBAR
          This panel is shown on large screens by default. It contains a form that listens
          for any text changes and immediately updates the portfolio's headings live using JavaScript!
        -->
        <aside id="customizer" class="w-80 bg-white dark:bg-apple-zinc border-r border-gold-200/40 dark:border-zinc-800 p-6 overflow-y-auto h-[calc(100vh-40px)] sticky top-10 z-40 transition-all duration-300 transform translate-x-0 hidden lg:block custom-scrollbar">
            <div class="flex justify-between items-center mb-6 border-b border-gold-100 dark:border-zinc-800 pb-4">
                <h3 class="text-lg font-serif font-bold text-gold-600 dark:text-gold-400 flex items-center gap-2">
                    <i class="fa-solid fa-sliders text-sm"></i> Live Content Editor
                </h3>
                <button onclick="toggleCustomizer()" class="lg:hidden text-gray-400 hover:text-red-500">
                    <i class="fa-solid fa-xmark text-lg"></i>
                </button>
            </div>

            <!-- This form triggers the JS function 'syncCustomizerFields()' every time you type -->
            <form id="customize-form" oninput="syncCustomizerFields()" class="space-y-5 text-sm">
                <div>
                    <label class="block font-semibold mb-1 text-xs uppercase tracking-wider text-gold-600 dark:text-gold-400">First Name</label>
                    <input type="text" id="input-firstName" value="Ninis" class="w-full bg-gold-50/50 dark:bg-zinc-900 border border-gold-200 dark:border-zinc-800 rounded p-2.5 focus:ring-1 focus:ring-gold-500 outline-none transition">
                </div>
                <div>
                    <label class="block font-semibold mb-1 text-xs uppercase tracking-wider text-gold-600 dark:text-gold-400">Last Name</label>
                    <input type="text" id="input-lastName" value="Twumasi" class="w-full bg-gold-50/50 dark:bg-zinc-900 border border-gold-200 dark:border-zinc-800 rounded p-2.5 focus:ring-1 focus:ring-gold-500 outline-none transition">
                </div>
                <div>
                    <label class="block font-semibold mb-1 text-xs uppercase tracking-wider text-gold-600 dark:text-gold-400">Academic Title</label>
                    <input type="text" id="input-academicTitle" value="Sophomore & CS Student at The Browning School" class="w-full bg-gold-50/50 dark:bg-zinc-900 border border-gold-200 dark:border-zinc-800 rounded p-2.5 focus:ring-1 focus:ring-gold-500 outline-none transition">
                </div>
                <div>
                    <label class="block font-semibold mb-1 text-xs uppercase tracking-wider text-gold-600 dark:text-gold-400">School Name</label>
                    <input type="text" id="input-school" value="The Browning School" class="w-full bg-gold-50/50 dark:bg-zinc-900 border border-gold-200 dark:border-zinc-800 rounded p-2.5 focus:ring-1 focus:ring-gold-500 outline-none transition">
                </div>
                <div>
                    <label class="block font-semibold mb-1 text-xs uppercase tracking-wider text-gold-600 dark:text-gold-400">Grade Level</label>
                    <input type="text" id="input-gradeLevel" value="Sophomore (Class of 2028)" class="w-full bg-gold-50/50 dark:bg-zinc-900 border border-gold-200 dark:border-zinc-800 rounded p-2.5 focus:ring-1 focus:ring-gold-500 outline-none transition">
                </div>
                <div>
                    <label class="block font-semibold mb-1 text-xs uppercase tracking-wider text-gold-600 dark:text-gold-400">Work Email Address</label>
                    <input type="email" id="input-email" value="ntwumasi@browning.edu" class="w-full bg-gold-50/50 dark:bg-zinc-900 border border-gold-200 dark:border-zinc-800 rounded p-2.5 focus:ring-1 focus:ring-gold-500 outline-none transition">
                </div>
                <div>
                    <label class="block font-semibold mb-1 text-xs uppercase tracking-wider text-gold-600 dark:text-gold-400">Interests & Hobbies</label>
                    <input type="text" id="input-hobbies" value="Soccer, Creative Writing, Track, Public Speaking, Community Activism" class="w-full bg-gold-50/50 dark:bg-zinc-900 border border-gold-200 dark:border-zinc-800 rounded p-2.5 focus:ring-1 focus:ring-gold-500 outline-none transition">
                </div>
                <div>
                    <label class="block font-semibold mb-1 text-xs uppercase tracking-wider text-gold-600 dark:text-gold-400">Core Career Goal</label>
                    <input type="text" id="input-careerGoal" value="To leverage storytelling, community engagement, and logic to drive social advocacy." class="w-full bg-gold-50/50 dark:bg-zinc-900 border border-gold-200 dark:border-zinc-800 rounded p-2.5 focus:ring-1 focus:ring-gold-500 outline-none transition">
                </div>
            </form>

            <div class="mt-6 pt-4 border-t border-gold-200/50 dark:border-zinc-800 space-y-2">
                <button onclick="resetToDefaults()" class="w-full py-2 border border-gold-300 dark:border-zinc-700 rounded-full hover:bg-gold-100 dark:hover:bg-zinc-800 transition font-medium text-xs text-gold-700 dark:text-gold-400">
                    Reset Parameters
                </button>
                <button onclick="window.print()" class="w-full py-2 bg-gold-500 text-apple-dark rounded-full hover:bg-gold-600 transition font-semibold text-xs flex items-center justify-center gap-1.5 shadow-sm">
                    <i class="fa-solid fa-print"></i> Export to PDF / Print
                </button>
            </div>
        </aside>

        <!-- Main Workspace containing header, sections, and footer -->
        <main class="flex-1 flex flex-col min-h-screen">
            
            <!-- 
              PROCESS: APPLE ELEGANCE MINIMAL NAVIGATION HEADER
              Sleek, blurred frosted glass header (`backdrop-blur-md`) that adapts 
              perfectly to both dark mode and light mode.
            -->
            <header class="bg-white/90 dark:bg-apple-dark/90 backdrop-blur-md border-b border-gold-200/20 dark:border-zinc-900 sticky top-0 z-30 transition-colors">
                <div class="max-w-6xl mx-auto px-6 py-4 flex justify-between items-center">
                    <a href="#" onclick="navigateTo('page-home')" class="flex items-center gap-2 font-bold text-lg tracking-tight hover:opacity-85 transition text-gold-600 dark:text-gold-400">
                        <span class="font-light text-gray-400">&lt;</span><span id="nav-logo-name">Ninis</span><span class="font-light text-gray-400">.js /&gt;</span>
                    </a>
                    
                    <!-- Desktop Header Navigation links -->
                    <div class="flex items-center gap-6">
                        <nav class="hidden md:flex items-center gap-8 text-xs font-semibold uppercase tracking-widest text-gray-600 dark:text-gray-300">
                            <a href="#" onclick="navigateTo('page-home')" class="nav-link hover:text-gold-500 transition duration-300">Home</a>
                            <a href="#" onclick="navigateTo('page-about')" class="nav-link hover:text-gold-500 transition duration-300">About</a>
                            <a href="#" onclick="navigateTo('page-resume')" class="nav-link hover:text-gold-500 transition duration-300">Resume</a>
                            <a href="#" onclick="navigateTo('page-skills')" class="nav-link hover:text-gold-500 transition duration-300">Skills</a>
                            <a href="#" onclick="navigateTo('page-projects')" class="nav-link hover:text-gold-500 transition duration-300">Projects</a>
                            <a href="#" onclick="navigateTo('page-contact')" class="nav-link hover:text-gold-500 transition duration-300">Contact</a>
                        </nav>

                        <!-- Control buttons on header -->
                        <div class="flex items-center gap-3 border-l border-gold-200/30 pl-4">
                            <!-- Toggle for side panel on mobile devices -->
                            <button onclick="toggleCustomizer()" class="lg:hidden text-gray-400 hover:text-gold-500 p-2 rounded-full hover:bg-gold-100/30" title="Edit Content">
                                <i class="fa-solid fa-sliders"></i>
                            </button>
                            <!-- Light/Dark Mode toggle button -->
                            <button onclick="toggleDarkMode()" class="text-gray-400 hover:text-gold-500 p-2 rounded-full hover:bg-gold-100/30 transition" title="Change Color Palette">
                                <i class="fa-solid fa-moon dark:hidden"></i>
                                <i class="fa-solid fa-sun hidden dark:inline"></i>
                            </button>
                            <!-- Full page elegant overlay menu button -->
                            <button onclick="openMenuOverlay()" class="text-gray-700 dark:text-gray-200 hover:text-gold-500 p-2 rounded-full hover:bg-gold-100/30 transition flex items-center gap-1.5">
                                <span class="text-[10px] font-bold tracking-widest uppercase hidden sm:inline">Menu</span>
                                <i class="fa-solid fa-bars-staggered text-lg"></i>
                            </button>
                        </div>
                    </div>
                </div>
            </header>

            <!-- 
              PROCESS: FULL-PAGE OVERLAY MENU (COVERING THE PAGE ITS ON)
              As requested, this is a premium full-screen layout built on a blurred glass element
              which pops over the current viewport when 'Menu' is clicked.
            -->
            <div id="full-menu-overlay" class="fixed inset-0 bg-white/98 dark:bg-apple-dark/98 backdrop-blur-2xl z-50 flex flex-col justify-between p-8 transition-all duration-500 opacity-0 pointer-events-none scale-95">
                <div class="flex justify-between items-center max-w-6xl w-full mx-auto">
                    <span class="font-bold text-xl tracking-tight text-gold-600 dark:text-gold-400 font-mono">&lt;Ninis.js /&gt;</span>
                    <button onclick="closeMenuOverlay()" class="w-12 h-12 rounded-full border border-gold-200/50 dark:border-zinc-850 flex items-center justify-center text-gray-500 hover:text-gold-500 dark:hover:text-gold-400 transition hover:rotate-90">
                        <i class="fa-solid fa-xmark text-lg"></i>
                    </button>
                </div>

                <!-- Main elegant menu links within overlay -->
                <nav class="flex flex-col items-center justify-center space-y-6 text-center my-auto">
                    <span class="text-[11px] font-bold text-gold-500 uppercase tracking-widest mb-2">Select Page Module</span>
                    <a href="#" onclick="navigateTo('page-home')" class="text-4xl sm:text-6xl font-serif font-light text-gray-800 dark:text-gray-100 hover:text-gold-500 transition tracking-tight">01 / Home</a>
                    <a href="#" onclick="navigateTo('page-about')" class="text-4xl sm:text-6xl font-serif font-light text-gray-800 dark:text-gray-100 hover:text-gold-500 transition tracking-tight">02 / About Me</a>
                    <a href="#" onclick="navigateTo('page-resume')" class="text-4xl sm:text-6xl font-serif font-light text-gray-800 dark:text-gray-100 hover:text-gold-500 transition tracking-tight">03 / Academic Resume</a>
                    <a href="#" onclick="navigateTo('page-skills')" class="text-4xl sm:text-6xl font-serif font-light text-gray-800 dark:text-gray-100 hover:text-gold-500 transition tracking-tight">04 / Core Skills</a>
                    <a href="#" onclick="navigateTo('page-projects')" class="text-4xl sm:text-6xl font-serif font-light text-gray-800 dark:text-gray-100 hover:text-gold-500 transition tracking-tight">05 / Projects &amp; Games</a>
                    <a href="#" onclick="navigateTo('page-contact')" class="text-4xl sm:text-6xl font-serif font-light text-gray-800 dark:text-gray-100 hover:text-gold-500 transition tracking-tight">06 / Contact Hub</a>
                </nav>

                <div class="text-center text-xs text-gray-400 max-w-xl mx-auto space-y-2">
                    <p class="font-mono text-gold-600">Pure, Lightweight HTML, CSS, and JS. Ready for GitHub Pages.</p>
                    <p>&copy; 2026 Ninis. All Rights Reserved.</p>
                </div>
            </div>

            <!-- 
              PROCESS: PAGE 1 (HOME PAGE SECTION)
              This section is active by default. It includes a dynamic background shuffle,
              introducing Ninis with modern clean typography and a responsive layout.
            -->
            <section id="page-home" class="page-container flex-1 bg-transition relative flex items-center py-16 md:py-28 min-h-[85vh]">
                <div class="max-w-6xl mx-auto px-6 w-full grid grid-cols-1 lg:grid-cols-12 gap-12 items-center relative z-10">
                    <div class="lg:col-span-7 space-y-6">
                        <div class="inline-flex items-center gap-2 bg-gold-100/80 dark:bg-gold-950/20 text-gold-700 dark:text-gold-400 px-4 py-1.5 rounded-full text-[10px] font-bold uppercase tracking-widest border border-gold-200/50">
                            <span class="w-2 h-2 rounded-full bg-gold-500 animate-pulse"></span>
                            Sophomore Portfolio
                        </div>
                        <h1 class="text-5xl sm:text-7xl font-serif font-light tracking-tight leading-none text-gray-900 dark:text-white">
                            Hi, I am <br><span class="font-bold text-transparent bg-clip-text bg-gradient-to-r from-gold-500 to-gold-700 display-firstName">Ninis</span> <span class="display-lastName">Twumasi</span>
                        </h1>
                        <p class="text-lg md:text-xl text-gray-600 dark:text-gray-300 font-light display-academicTitle tracking-wide">
                            Sophomore &amp; CS Student at The Browning School
                        </p>
                        <p class="text-gray-500 dark:text-gray-400 leading-relaxed max-w-xl text-sm font-light">
                            Welcome to My Website! This platform is 100% designed and coded by me to reflect who I am—a 15-year-old student from Manhattan, NYC, doing my best to make a lasting impact both in and out of the classroom.
                        </p>
                        <div class="flex flex-wrap gap-4 pt-4">
                            <button onclick="navigateTo('page-about')" class="px-8 py-3.5 bg-gold-500 hover:bg-gold-600 text-apple-dark text-xs font-bold uppercase tracking-wider rounded-full shadow-lg hover:shadow-gold-500/20 transition flex items-center gap-2">
                                Explore About Me <i class="fa-solid fa-arrow-right"></i>
                            </button>
                            <!-- This button calls Javascript to pick a random luxury gold texture as background -->
                            <button onclick="shuffleBackground()" class="px-6 py-3.5 bg-white/85 dark:bg-zinc-900/85 backdrop-blur text-gold-600 dark:text-gold-400 border border-gold-200 dark:border-zinc-800 hover:border-gold-500 text-xs font-bold uppercase tracking-wider rounded-full transition flex items-center gap-2 shadow-sm">
                                <i class="fa-solid fa-wand-magic-sparkles"></i> Shuffle Background
                            </button>
                        </div>
                    </div>

                    <!-- 
                      PROCESS: INTERACTIVE PYTHON CONSOLE TERMINAL
                      Provides a visual interface running mock terminal scripts.
                    -->
                    <div class="lg:col-span-5 w-full">
                        <div class="bg-white/80 dark:bg-zinc-950/80 backdrop-blur-md rounded-2xl overflow-hidden shadow-2xl border border-gold-200/30 dark:border-zinc-800/80 flex flex-col font-mono text-xs sm:text-sm">
                            <div class="bg-gold-100/40 dark:bg-zinc-900/60 px-4 py-3 flex justify-between items-center border-b border-gold-200/20 dark:border-zinc-800">
                                <div class="flex gap-2">
                                    <span class="w-2.5 h-2.5 rounded-full bg-red-400"></span>
                                    <span class="w-2.5 h-2.5 rounded-full bg-yellow-400"></span>
                                    <span class="w-2.5 h-2.5 rounded-full bg-green-400"></span>
                                </div>
                                <span class="text-gray-400 font-semibold text-[10px] tracking-wider uppercase font-sans">
                                    <i class="fa-brands fa-python text-gold-500 mr-1"></i> console.py
                                </span>
                                <span class="w-6"></span>
                            </div>
                            <div class="p-6 space-y-4 text-gold-700 dark:text-gold-400 bg-white/50 dark:bg-zinc-950/30">
                                <div>
                                    <span class="text-purple-600 dark:text-purple-400">class</span> <span class="text-gold-600 dark:text-gold-200">Portfolio</span>:
                                </div>
                                <div class="pl-4">
                                    <span class="text-purple-600 dark:text-purple-400">def</span> <span class="text-gold-600 dark:text-gold-200">__init__</span>(<span class="text-gray-500">self</span>):
                                </div>
                                <div class="pl-8 text-gray-500 dark:text-zinc-500">
                                    <span class="text-gray-400">self</span>.owner = <span class="text-green-600 dark:text-green-400">"<span class="display-fullName">Ninis Twumasi</span>"</span><br>
                                    <span class="text-gray-400">self</span>.age = <span class="text-green-600 dark:text-green-400">15</span><br>
                                    <span class="text-gray-400">self</span>.school = <span class="text-green-600 dark:text-green-400">"The Browning School"</span>
                                </div>
                                <div class="border-t border-gold-200/20 dark:border-zinc-850 pt-3 text-[10px] text-gray-400 font-sans">
                                    # Click run button below to execute dynamic Javascript console simulation
                                </div>
                                <div class="bg-gold-50/50 dark:bg-zinc-900/50 p-3 rounded-xl border border-gold-200/20 dark:border-zinc-800 text-xs">
                                    <div id="py-output" class="text-gray-700 dark:text-gray-300">Press button below to execute logic parameters...</div>
                                </div>
                                <button onclick="executePyDemo()" class="w-full py-2 bg-gold-500 hover:bg-gold-600 text-apple-dark text-xs font-semibold uppercase tracking-wider rounded-lg transition font-sans">
                                    Run Console Simulation
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- 
              PROCESS: PAGE 2 (ABOUT ME SECTION)
              This section displays your comprehensive biography, including your sophomore 
              status at Browning, extracurricular interests, and community recovery activism.
            -->
            <section id="page-about" class="page-container flex-1 py-20 bg-white dark:bg-apple-dark transition-colors hidden">
                <div class="max-w-6xl mx-auto px-6">
                    <div class="text-center max-w-2xl mx-auto mb-16">
                        <span class="text-[10px] font-bold text-gold-500 uppercase tracking-widest">About the Programmer</span>
                        <h2 class="text-4xl font-serif font-light tracking-tight text-gray-900 dark:text-white mt-2">Ninis Twumasi</h2>
                        <div class="w-12 h-[2px] bg-gold-400 mx-auto rounded mt-3"></div>
                    </div>

                    <div class="grid grid-cols-1 md:grid-cols-12 gap-12 items-center">
                        <!-- Left: Elegant Avatar visual -->
                        <div class="md:col-span-5 flex flex-col items-center">
                            <div class="relative group">
                                <div class="absolute -inset-1 bg-gradient-to-r from-gold-300 to-gold-600 rounded-2xl blur opacity-30 group-hover:opacity-50 transition duration-1000"></div>
                                <div class="relative bg-white dark:bg-zinc-900 p-2 rounded-2xl border border-gold-200/50 dark:border-zinc-800">
                                    <div class="w-64 h-64 bg-gold-100/50 dark:bg-zinc-800/50 rounded-xl overflow-hidden flex items-center justify-center relative border border-gold-200/30">
                                        <svg class="w-32 h-32 text-gold-500/80" fill="currentColor" viewBox="0 0 24 24">
                                            <path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/>
                                        </svg>
                                        <div class="absolute bottom-4 bg-white/90 dark:bg-zinc-900/90 backdrop-blur text-gold-600 dark:text-gold-400 text-[9px] uppercase font-bold py-1.5 px-3.5 rounded-full border border-gold-200/50 dark:border-zinc-700 font-mono tracking-wider">
                                            Browning Sophomore
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Right: Detailed school biography (with strict academic alignment) -->
                        <div class="md:col-span-7 space-y-6">
                            <h3 class="text-2xl font-serif font-light text-gray-800 dark:text-gray-200 tracking-wide">
                                Manhattan Student &amp; Community Advocate
                            </h3>
                            <p class="text-gray-600 dark:text-gray-300 leading-relaxed font-light text-sm display-aboutBio">
                                This website is coded 100% by me and is a reflection of who I am, a 15-year-old student from Manhattan, NYC, doing my best to make an impact both in and out of the classroom. I'm currently a sophomore at The Browning School, where I stay busy between classes, soccer, track, and everything in between. Community is at the core of who I am. When asked about me in a few words to describe me, I am called kind-hearted, charismatic, persistent, driven, and determined. Whenever I am motivated about something, I always see it through. In addition, whenever someone needs me, I am always there for them.
                            </p>
                            <p class="text-gray-600 dark:text-gray-300 leading-relaxed font-light text-sm">
                                As a student at Browning, I feel a real responsibility to use the opportunities I've been given to give back. Whether that's through founding Browning's Food Recovery Program with Grassroots Grocery, representing the Black Student Coalition across NYC, or showing up to local fundraisers and charity events, I believe giving back isn't something I do on the side; it's an important part of who I am.
                            </p>
                            <p class="text-gray-600 dark:text-gray-300 leading-relaxed font-light text-sm">
                                Outside of activism, I'm an advocate at heart. I've spent years fighting for what I believe in and always helping people whenever they seek help. I personally find purpose in helping people with issues, no matter how small. Today, I spend my time writing creatively, playing soccer, spending time with friends, and staying up to date with world issues today and what we can do to help.
                            </p>
                            
                            <div class="grid grid-cols-1 sm:grid-cols-2 gap-6 pt-6 border-t border-gold-200/20 dark:border-zinc-800">
                                <div>
                                    <h4 class="font-semibold text-xs uppercase tracking-wider text-gold-600 dark:text-gold-400 flex items-center gap-2 mb-2">
                                        <i class="fa-solid fa-gamepad"></i> Hobbies &amp; Interests
                                    </h4>
                                    <p class="text-xs text-gray-500 dark:text-gray-400 display-hobbies leading-relaxed font-light">
                                        Soccer, Creative Writing, Track, Public Speaking, Community Activism
                                    </p>
                                </div>
                                <div>
                                    <h4 class="font-semibold text-xs uppercase tracking-wider text-gold-600 dark:text-gold-400 flex items-center gap-2 mb-2">
                                        <i class="fa-solid fa-bullseye"></i> Core Career Goal
                                    </h4>
                                    <p class="text-xs text-gray-500 dark:text-gray-400 display-careerGoal leading-relaxed font-light">
                                        To leverage storytelling, community engagement, and logic to drive social advocacy.
                                    </p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- 
              PROCESS: PAGE 3 (RESUME SECTION)
              Fulfills the rubric criteria for a clear academic resume styling.
              Includes school, grade level, and coursework, plus your role at Camp KenMont.
            -->
            <section id="page-resume" class="page-container flex-1 py-20 bg-gold-100/30 dark:bg-apple-dark/60 transition-colors hidden">
                <div class="max-w-6xl mx-auto px-6">
                    <div class="text-center max-w-2xl mx-auto mb-16">
                        <span class="text-[10px] font-bold text-gold-500 uppercase tracking-widest">Academic & Activity Curriculum</span>
                        <h2 class="text-4xl font-serif font-light tracking-tight text-gray-900 dark:text-white mt-2">Resume & Experience</h2>
                        <div class="w-12 h-[2px] bg-gold-400 mx-auto rounded mt-3"></div>
                        <p class="text-sm text-gray-400 mt-2">Dedicated and driven student with strong communication and problem-solving skills.</p>
                    </div>

                    <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
                        <!-- Column 1: Education & Work Experience -->
                        <div class="space-y-6">
                            <div class="bg-white dark:bg-apple-zinc p-8 rounded-2xl shadow-sm border border-gold-200/30 dark:border-zinc-850">
                                <div class="flex items-center gap-3 border-b border-gold-100 dark:border-zinc-800 pb-3 mb-4">
                                    <span class="bg-gold-100 dark:bg-zinc-800 text-gold-600 dark:text-gold-400 w-10 h-10 rounded-full flex items-center justify-center text-md">
                                        <i class="fa-solid fa-graduation-cap"></i>
                                    </span>
                                    <div>
                                        <h3 class="font-semibold text-base">Education</h3>
                                        <p class="text-[9px] text-gray-400 uppercase tracking-widest font-mono">Schooling timeline</p>
                                    </div>
                                </div>
                                <div class="relative pl-4 border-l-2 border-gold-500 py-1">
                                    <h4 class="font-semibold text-sm display-school">The Browning School</h4>
                                    <p class="text-xs text-gray-500 mt-0.5 font-mono">2021 – 2026</p>
                                    <p class="text-xs text-gray-400 mt-1 font-mono text-[10px]">Sophomore (Class of 2028)</p>
                                    <p class="text-xs text-gray-400 mt-2">Nurturing academic curiosity, community stewardship, and leadership.</p>
                                </div>
                            </div>

                            <div class="bg-white dark:bg-apple-zinc p-8 rounded-2xl shadow-sm border border-gold-200/30 dark:border-zinc-850">
                                <div class="flex items-center gap-3 border-b border-gold-100 dark:border-zinc-800 pb-3 mb-4">
                                    <span class="bg-gold-100 dark:bg-zinc-800 text-gold-600 dark:text-gold-400 w-10 h-10 rounded-full flex items-center justify-center text-md">
                                        <i class="fa-solid fa-briefcase"></i>
                                    </span>
                                    <div>
                                        <h3 class="font-semibold text-base">Work Experience</h3>
                                        <p class="text-[9px] text-gray-400 uppercase tracking-widest font-mono">Employment</p>
                                    </div>
                                </div>
                                <div class="relative pl-4 border-l-2 border-gold-500 py-1">
                                    <h4 class="font-semibold text-sm">Camp Counselor</h4>
                                    <p class="text-xs text-gray-500 font-semibold font-mono">Camp KenMont and KenWood</p>
                                    <p class="text-xs text-gray-400 font-mono">Summer 2026</p>
                                    <p class="text-xs text-gray-400 mt-2 leading-relaxed">
                                        Serving as a Camp Counselor from July 19th to August 16th. Having attended the camp for the past two years, I look forward to giving back to the community that has positively impacted me. This experience will allow me to develop leadership, responsibility, and mentorship skills while working closely with children in a team-oriented environment.
                                    </p>
                                </div>
                            </div>
                        </div>

                        <!-- Column 2: Leadership & Advocacy Roles -->
                        <div class="space-y-6">
                            <div class="bg-white dark:bg-apple-zinc p-8 rounded-2xl shadow-sm border border-gold-200/30 dark:border-zinc-850">
                                <div class="flex items-center gap-3 border-b border-gold-100 dark:border-zinc-800 pb-3 mb-4">
                                    <span class="bg-gold-100 dark:bg-zinc-800 text-gold-600 dark:text-gold-400 w-10 h-10 rounded-full flex items-center justify-center text-md">
                                        <i class="fa-solid fa-users-gear"></i>
                                    </span>
                                    <div>
                                        <h3 class="font-semibold text-base">Leadership Roles</h3>
                                        <p class="text-[9px] text-gray-400 uppercase tracking-widest font-mono">Student Advocacy</p>
                                    </div>
                                </div>

                                <div class="space-y-5">
                                    <div class="relative pl-4 border-l border-gold-500">
                                        <h4 class="font-semibold text-xs">Soccer JV Captain (2025)</h4>
                                        <p class="text-[11px] text-gray-400 mt-1 leading-relaxed">
                                            Played competitive soccer for over six years, developing strong teamwork, communication, and leadership. Served as JV Captain, helping lead practices and motivate teammates.
                                        </p>
                                    </div>
                                    <div class="relative pl-4 border-l border-gold-500">
                                        <h4 class="font-semibold text-xs">Black Student Coalition NYC Rep (2025–2026)</h4>
                                        <p class="text-[11px] text-gray-400 mt-1 leading-relaxed">
                                            Serve as Browning's representative to connect Black students across New York City. Promote Black culture, encourage meaningful discussions, and help build a supportive and empowering community.
                                        </p>
                                    </div>
                                    <div class="relative pl-4 border-l border-gold-500">
                                        <h4 class="font-semibold text-xs">Founder, Browning Food Recovery Program</h4>
                                        <p class="text-[11px] text-gray-400 mt-1 leading-relaxed">
                                            Founded the food recovery program in partnership with Grassroots Grocery to combat food insecurity and redirect unused resources toward supporting local communities.
                                        </p>
                                    </div>
                                    <div class="relative pl-4 border-l border-gold-500">
                                        <h4 class="font-semibold text-xs">Chief Editor, MS Newspaper (2021–2024)</h4>
                                        <p class="text-[11px] text-gray-400 mt-1 leading-relaxed">
                                            Founded and led Browning’s Middle School newspaper out of a passion for storytelling and sharing information. Oversaw article creation, editing, and publication.
                                        </p>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Column 3: Organizations & Academic Pursuits -->
                        <div class="space-y-6">
                            <div class="bg-white dark:bg-apple-zinc p-8 rounded-2xl shadow-sm border border-gold-200/30 dark:border-zinc-850">
                                <div class="flex items-center gap-3 border-b border-gold-100 dark:border-zinc-800 pb-3 mb-4">
                                    <span class="bg-gold-100 dark:bg-zinc-800 text-gold-600 dark:text-gold-400 w-10 h-10 rounded-full flex items-center justify-center text-md">
                                        <i class="fa-solid fa-star"></i>
                                    </span>
                                    <div>
                                        <h3 class="font-semibold text-base">Clubs &amp; Pursuits</h3>
                                        <p class="text-[9px] text-gray-400 uppercase tracking-widest font-mono">Academic Engagement</p>
                                    </div>
                                </div>

                                <div class="space-y-5">
                                    <div class="relative pl-4 border-l border-gold-500">
                                        <h4 class="font-semibold text-xs">Time for Kids Reporter (2023–2024)</h4>
                                        <p class="text-[11px] text-gray-400 mt-1">Contributed articles focused on current events and topics I am passionate about in order to spread awareness and inform readers. Strengthened my writing and journalism.</p>
                                    </div>
                                    <div class="relative pl-4 border-l border-gold-500">
                                        <h4 class="font-semibold text-xs">Mock Trial (2023–2026)</h4>
                                        <p class="text-[11px] text-gray-400 mt-1">Developed skills in public speaking, reasoning, advocacy, and critical thinking. Learned how to build arguments and present confidently under pressure.</p>
                                    </div>
                                    <div class="relative pl-4 border-l border-gold-500">
                                        <h4 class="font-semibold text-xs">Debate Team (2024–2026)</h4>
                                        <p class="text-[11px] text-gray-400 mt-1">Competed in debates focused on argumentation, public speaking, and analytical reasoning. Improved my ability to think critically and defend positions.</p>
                                    </div>
                                    <div class="relative pl-4 border-l border-gold-500">
                                        <h4 class="font-semibold text-xs">Varsity Indoor/Outdoor Track (2025–2026)</h4>
                                        <p class="text-[11px] text-gray-400 mt-1">Competed while focusing on discipline, perseverance, and personal growth. Worked toward improving performance and maintaining physical fitness.</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- 
              PROCESS: PAGE 4 (SKILLS SECTION WITH REAL INTERACTIVE CATEGORY FILTERING)
              Users can select different categories (All, Tech & Creative, Academic, Leadership).
              We use Tailwind width transition styles to animate the golden metrics rating bars!
            -->
            <section id="page-skills" class="page-container flex-1 py-20 bg-white dark:bg-apple-dark transition-colors hidden">
                <div class="max-w-6xl mx-auto px-6">
                    <div class="text-center max-w-2xl mx-auto mb-12">
                        <span class="text-[10px] font-bold text-gold-500 uppercase tracking-widest">Skill Metrics</span>
                        <h2 class="text-4xl font-serif font-light tracking-tight text-gray-900 dark:text-white mt-2">Competencies &amp; Abilities</h2>
                        <div class="w-12 h-[2px] bg-gold-400 mx-auto rounded mt-3"></div>
                    </div>

                    <!-- Interactive Skill Filters -->
                    <div class="flex justify-center gap-3 mb-12 flex-wrap">
                        <button onclick="filterSkills('all')" class="filter-btn px-5 py-2 bg-gold-500 text-apple-dark text-xs font-bold uppercase tracking-widest rounded-full transition shadow-sm">All</button>
                        <button onclick="filterSkills('tech')" class="filter-btn px-5 py-2 bg-white dark:bg-zinc-900 border border-gold-200 dark:border-zinc-800 text-gray-600 dark:text-gray-300 text-xs font-bold uppercase tracking-widest rounded-full transition hover:border-gold-500">Tech &amp; Creative</button>
                        <button onclick="filterSkills('academic')" class="filter-btn px-5 py-2 bg-white dark:bg-zinc-900 border border-gold-200 dark:border-zinc-800 text-gray-600 dark:text-gray-300 text-xs font-bold uppercase tracking-widest rounded-full transition hover:border-gold-500">Academic &amp; Speaking</button>
                        <button onclick="filterSkills('personal')" class="filter-btn px-5 py-2 bg-white dark:bg-zinc-900 border border-gold-200 dark:border-zinc-800 text-gray-600 dark:text-gray-300 text-xs font-bold uppercase tracking-widest rounded-full transition hover:border-gold-500">Leadership</button>
                    </div>

                    <div class="grid grid-cols-1 md:grid-cols-3 gap-8" id="skills-grid">
                        <!-- Tech / Creative Skills -->
                        <div class="skill-card bg-gold-100/20 dark:bg-zinc-900/40 p-8 rounded-2xl border border-gold-200/20 dark:border-zinc-850 space-y-4 transition-all duration-300" data-category="tech">
                            <h3 class="font-semibold text-sm text-gold-600 dark:text-gold-400 flex items-center gap-2 border-b border-gold-200/20 dark:border-zinc-800 pb-2">
                                <i class="fa-solid fa-laptop-code text-gold-500"></i> Tech &amp; Creative
                            </h3>
                            <div class="space-y-4">
                                <div>
                                    <div class="flex justify-between text-xs mb-1">
                                        <span class="font-mono">Python Coding</span>
                                        <span class="font-bold">Basic</span>
                                    </div>
                                    <div class="w-full bg-gold-200/30 dark:bg-zinc-800 h-[3px] rounded-full overflow-hidden">
                                        <div class="bg-gold-500 h-full rounded-full" style="width: 75%;"></div>
                                    </div>
                                </div>
                                <div>
                                    <div class="flex justify-between text-xs mb-1">
                                        <span class="font-mono">HTML &amp; CSS Structure</span>
                                        <span class="font-bold">Good</span>
                                    </div>
                                    <div class="w-full bg-gold-200/30 dark:bg-zinc-800 h-[3px] rounded-full overflow-hidden">
                                        <div class="bg-gold-500 h-full rounded-full" style="width: 85%;"></div>
                                    </div>
                                </div>
                                <div>
                                    <div class="flex justify-between text-xs mb-1">
                                        <span class="font-mono">Onshape CAD Program</span>
                                        <span class="font-bold">Proficient</span>
                                    </div>
                                    <div class="w-full bg-gold-200/30 dark:bg-zinc-800 h-[3px] rounded-full overflow-hidden">
                                        <div class="bg-gold-500 h-full rounded-full" style="width: 80%;"></div>
                                    </div>
                                </div>
                                <div>
                                    <div class="flex justify-between text-xs mb-1">
                                        <span class="font-mono">Creative Journalism</span>
                                        <span class="font-bold">Excellent</span>
                                    </div>
                                    <div class="w-full bg-gold-200/30 dark:bg-zinc-800 h-[3px] rounded-full overflow-hidden">
                                        <div class="bg-gold-500 h-full rounded-full" style="width: 90%;"></div>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Academic Skills -->
                        <div class="skill-card bg-gold-100/20 dark:bg-zinc-900/40 p-8 rounded-2xl border border-gold-200/20 dark:border-zinc-850 space-y-4 transition-all duration-300" data-category="academic">
                            <h3 class="font-semibold text-sm text-gold-600 dark:text-gold-400 flex items-center gap-2 border-b border-gold-200/20 dark:border-zinc-800 pb-2">
                                <i class="fa-solid fa-brain text-gold-500"></i> Academic &amp; Speaking
                            </h3>
                            <div class="space-y-4">
                                <div>
                                    <div class="flex justify-between text-xs mb-1">
                                        <span>French (Language)</span>
                                        <span class="font-bold">Intermediate</span>
                                    </div>
                                    <div class="w-full bg-gold-200/30 dark:bg-zinc-800 h-[3px] rounded-full overflow-hidden">
                                        <div class="bg-gold-500 h-full rounded-full" style="width: 65%;"></div>
                                    </div>
                                </div>
                                <div>
                                    <div class="flex justify-between text-xs mb-1">
                                        <span>Public Speaking &amp; Debate</span>
                                        <span class="font-bold">Advocate</span>
                                    </div>
                                    <div class="w-full bg-gold-200/30 dark:bg-zinc-800 h-[3px] rounded-full overflow-hidden">
                                        <div class="bg-gold-500 h-full rounded-full" style="width: 95%;"></div>
                                    </div>
                                </div>
                                <div>
                                    <div class="flex justify-between text-xs mb-1">
                                        <span>Research &amp; Fact-Checking</span>
                                        <span class="font-bold">Detailed</span>
                                    </div>
                                    <div class="w-full bg-gold-200/30 dark:bg-zinc-800 h-[3px] rounded-full overflow-hidden">
                                        <div class="bg-gold-500 h-full rounded-full" style="width: 90%;"></div>
                                    </div>
                                </div>
                                <div>
                                    <div class="flex justify-between text-xs mb-1">
                                        <span>Scientific Writing</span>
                                        <span class="font-bold">Strong</span>
                                    </div>
                                    <div class="w-full bg-gold-200/30 dark:bg-zinc-800 h-[3px] rounded-full overflow-hidden">
                                        <div class="bg-gold-500 h-full rounded-full" style="width: 80%;"></div>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Personal Skills -->
                        <div class="skill-card bg-gold-100/20 dark:bg-zinc-900/40 p-8 rounded-2xl border border-gold-200/20 dark:border-zinc-850 space-y-4 transition-all duration-300" data-category="personal">
                            <h3 class="font-semibold text-sm text-gold-600 dark:text-gold-400 flex items-center gap-2 border-b border-gold-200/20 dark:border-zinc-800 pb-2">
                                <i class="fa-solid fa-people-arrows text-gold-500"></i> Leadership &amp; Community
                            </h3>
                            <div class="space-y-4">
                                <div>
                                    <div class="flex justify-between text-xs mb-1">
                                        <span>Community Organizing</span>
                                        <span class="font-bold">Exceptional</span>
                                    </div>
                                    <div class="w-full bg-gold-200/30 dark:bg-zinc-800 h-[3px] rounded-full overflow-hidden">
                                        <div class="bg-gold-500 h-full rounded-full" style="width: 95%;"></div>
                                    </div>
                                </div>
                                <div>
                                    <div class="flex justify-between text-xs mb-1">
                                        <span>Team Leadership &amp; Mentorship</span>
                                        <span class="font-bold">Active</span>
                                    </div>
                                    <div class="w-full bg-gold-200/30 dark:bg-zinc-800 h-[3px] rounded-full overflow-hidden">
                                        <div class="bg-gold-500 h-full rounded-full" style="width: 90%;"></div>
                                    </div>
                                </div>
                                <div>
                                    <div class="flex justify-between text-xs mb-1">
                                        <span>Advocacy &amp; Mediation</span>
                                        <span class="font-bold">Driven</span>
                                    </div>
                                    <div class="w-full bg-gold-200/30 dark:bg-zinc-800 h-[3px] rounded-full overflow-hidden">
                                        <div class="bg-gold-500 h-full rounded-full" style="width: 88%;"></div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- 
              PROCESS: PAGE 5 (PROJECTS & FLOWCHART PORTFOLIO SECTION)
              This renders your CS portfolio projects. 
              Includes an interactive Python-styled Guessing Game, a live Sorting visualizer, 
              and a structural flowchart representing your software components.
            -->
            <section id="page-projects" class="page-container flex-1 py-20 bg-gold-50 text-gray-900 dark:bg-apple-dark transition-colors hidden">
                <div class="max-w-6xl mx-auto px-6">
                    <div class="text-center max-w-2xl mx-auto mb-16">
                        <span class="text-[10px] font-bold text-gold-500 uppercase tracking-widest">Functional Demos</span>
                        <h2 class="text-4xl font-serif font-light tracking-tight text-gray-900 dark:text-white mt-2">Projects &amp; Logic Maps</h2>
                        <div class="w-12 h-[2px] bg-gold-400 mx-auto rounded mt-3"></div>
                    </div>

                    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                        <!-- Project 1: Guessing Game -->
                        <div class="bg-white dark:bg-apple-zinc rounded-2xl overflow-hidden shadow-sm border border-gold-200/30 dark:border-zinc-850 flex flex-col justify-between">
                            <div class="p-6 space-y-4">
                                <div class="flex justify-between items-start">
                                    <span class="bg-gold-100 dark:bg-gold-950/40 text-gold-700 dark:text-gold-400 text-[10px] font-mono font-bold px-2.5 py-1 rounded-full border border-gold-200/20">JS Engine</span>
                                    <span class="text-gray-400 text-xs"><i class="fa-solid fa-calendar-days mr-1"></i> CSE Final</span>
                                </div>
                                <h3 class="font-semibold text-base">Interactive Guessing Game</h3>
                                <p class="text-xs text-gray-500 dark:text-gray-400 leading-relaxed font-light">
                                    A high-performance digital guess-the-number game built with input validation controls. Perfect representation of binary search algorithmic principles.
                                </p>
                            </div>
                            
                            <!-- Mini Game Inside Card -->
                            <div class="p-4 bg-gold-100/10 dark:bg-zinc-950/40 border-t border-gold-200/20 dark:border-zinc-800">
                                <div class="bg-zinc-950 text-gold-400 p-3 rounded-xl font-mono text-[11px] h-36 flex flex-col justify-between">
                                    <div id="game-display" class="overflow-y-auto h-24 custom-scrollbar whitespace-pre-wrap">System: Guess the secret number from 1 to 20!</div>
                                    <div class="flex gap-2">
                                        <input type="number" id="game-guess-input" min="1" max="20" placeholder="Guess" class="w-full bg-zinc-900 text-white rounded px-2.5 py-1 text-xs border border-zinc-800 outline-none">
                                        <button onclick="playMiniGame()" class="bg-gold-500 hover:bg-gold-600 text-apple-dark text-xs px-3.5 py-1.5 rounded-lg font-sans font-semibold transition">Submit</button>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Project 2: Sorting array step-by-step -->
                        <div class="bg-white dark:bg-apple-zinc rounded-2xl overflow-hidden shadow-sm border border-gold-200/30 dark:border-zinc-850 flex flex-col justify-between">
                            <div class="p-6 space-y-4">
                                <div class="flex justify-between items-start">
                                    <span class="bg-gold-100 dark:bg-gold-950/40 text-gold-700 dark:text-gold-400 text-[10px] font-mono font-bold px-2.5 py-1 rounded-full border border-gold-200/20">Visualization</span>
                                    <span class="text-gray-400 text-xs"><i class="fa-solid fa-bolt mr-1"></i> Step Engine</span>
                                </div>
                                <h3 class="font-semibold text-base">Sorting Flow Visualizer</h3>
                                <p class="text-xs text-gray-500 dark:text-gray-400 leading-relaxed font-light">
                                    Watch real-time sorting logic step through arrays dynamically inside modern containers. Fully visualizes the inner execution of simple sorting algorithms.
                                </p>
                            </div>

                            <div class="p-4 bg-gold-100/10 dark:bg-zinc-950/40 border-t border-gold-200/20 dark:border-zinc-800">
                                <div class="p-3 bg-white dark:bg-zinc-900 rounded-xl border border-gold-200/20 dark:border-zinc-800">
                                    <div class="flex justify-between items-end gap-2 h-16 pb-2" id="sorting-bars">
                                        <!-- Bars rendered on load -->
                                    </div>
                                    <div class="flex justify-between items-center mt-3">
                                        <span class="text-[10px] text-gray-400 font-mono" id="sorting-status">Idle</span>
                                        <button onclick="startBubbleSortSim()" class="text-xs text-gold-600 dark:text-gold-400 font-semibold flex items-center gap-1 hover:opacity-80 transition">
                                            <i class="fa-solid fa-play text-[10px]"></i> Step Algorithm
                                        </button>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Project 3: Flow diagram system architectural setup -->
                        <div class="bg-white dark:bg-apple-zinc rounded-2xl overflow-hidden shadow-sm border border-gold-200/30 dark:border-zinc-850 flex flex-col justify-between">
                            <div class="p-6 space-y-4">
                                <div class="flex justify-between items-start">
                                    <span class="bg-gold-100 dark:bg-gold-950/40 text-gold-700 dark:text-gold-400 text-[10px] font-mono font-bold px-2.5 py-1 rounded-full border border-gold-200/20">System architecture</span>
                                    <span class="text-gray-400 text-xs"><i class="fa-solid fa-diagram-project mr-1"></i> Flow Diagram</span>
                                </div>
                                <h3 class="font-semibold text-base">CSE Data Flow Control</h3>
                                <p class="text-xs text-gray-500 dark:text-gray-400 leading-relaxed font-light">
                                    Design architecture showing systemic processing workflows across browser-level interactions. Demonstrates core flowchart principles.
                                </p>
                            </div>

                            <div class="p-4 bg-gold-100/10 dark:bg-zinc-950/40 border-t border-gold-200/20 dark:border-zinc-800">
                                <div class="bg-white dark:bg-zinc-900 p-3 rounded-xl border border-gold-200/20 dark:border-zinc-800 text-[10px] font-mono space-y-2">
                                    <div class="flex justify-between items-center border border-dashed border-gold-200/30 p-1 bg-gold-50/50 dark:bg-zinc-950/50">
                                        <span class="text-gold-600 font-bold">START</span>
                                        <i class="fa-solid fa-arrow-right text-[9px] text-gray-400"></i>
                                        <span>User Selects Tab</span>
                                    </div>
                                    <div class="flex justify-between items-center border border-dashed border-gold-200/30 p-1">
                                        <span>Execute Router</span>
                                        <i class="fa-solid fa-arrow-right text-[9px] text-gray-400"></i>
                                        <span class="text-gold-500">Display Page</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- 
              PROCESS: PAGE 6 (CONTACT HUB HUB)
              This section contains work emails, personal emails, your LinkedIn profile link,
              and a fully styled messaging interface.
            -->
            <section id="page-contact" class="page-container flex-1 py-20 bg-white dark:bg-apple-dark transition-colors hidden">
                <div class="max-w-4xl mx-auto px-6">
                    <div class="text-center max-w-2xl mx-auto mb-16">
                        <span class="text-[10px] font-bold text-gold-500 uppercase tracking-widest">Connect with me</span>
                        <h2 class="text-4xl font-serif font-light tracking-tight text-gray-900 dark:text-white mt-2">Get in Touch</h2>
                        <div class="w-12 h-[2px] bg-gold-400 mx-auto rounded mt-3"></div>
                        <p class="text-sm text-gray-400 mt-2">Have a question or want to connect? Feel free to reach out.</p>
                    </div>

                    <div class="grid grid-cols-1 md:grid-cols-3 gap-8 mb-12">
                        <!-- Work Email -->
                        <div class="bg-gold-50 dark:bg-apple-zinc p-6 rounded-2xl border border-gold-200/30 text-center space-y-2">
                            <i class="fa-solid fa-envelope text-gold-500 text-2xl"></i>
                            <h4 class="font-semibold text-xs uppercase tracking-wider text-gray-500">Work Email</h4>
                            <p class="text-sm font-semibold text-gold-600 dark:text-gold-400 break-all select-all">ntwumasi@browning.edu</p>
                        </div>
                        <!-- Personal Email -->
                        <div class="bg-gold-50 dark:bg-apple-zinc p-6 rounded-2xl border border-gold-200/30 text-center space-y-2">
                            <i class="fa-solid fa-envelope-open text-gold-500 text-2xl"></i>
                            <h4 class="font-semibold text-xs uppercase tracking-wider text-gray-500">Personal Email</h4>
                            <p class="text-sm font-semibold text-gold-600 dark:text-gold-400 break-all select-all">ninist2010@gmail.com</p>
                        </div>
                        <!-- LinkedIn -->
                        <div class="bg-gold-50 dark:bg-apple-zinc p-6 rounded-2xl border border-gold-200/30 text-center space-y-2">
                            <i class="fa-brands fa-linkedin text-gold-500 text-2xl"></i>
                            <h4 class="font-semibold text-xs uppercase tracking-wider text-gray-500">LinkedIn</h4>
                            <a href="https://www.linkedin.com/in/ninis-twumasi-477346365" target="_blank" rel="noopener noreferrer" class="text-xs font-semibold text-gold-600 dark:text-gold-400 hover:underline inline-block break-all">
                                view profile
                            </a>
                        </div>
                    </div>

                    <div class="bg-gold-50 dark:bg-apple-zinc rounded-2xl p-8 border border-gold-200/30 dark:border-zinc-850">
                        <form id="contact-form" onsubmit="handleContactSubmit(event)" class="space-y-6">
                            <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
                                <div>
                                    <label class="block text-[10px] uppercase tracking-wider text-gray-500 mb-2 font-semibold">Your Name</label>
                                    <input type="text" required placeholder="John Doe" class="w-full bg-white dark:bg-zinc-950 border border-gold-200/30 dark:border-zinc-800 rounded-xl p-3 outline-none focus:ring-1 focus:ring-gold-500 text-sm">
                                </div>
                                <div>
                                    <label class="block text-[10px] uppercase tracking-wider text-gray-500 mb-2 font-semibold">Your Email Address</label>
                                    <input type="email" required placeholder="visitor@example.com" class="w-full bg-white dark:bg-zinc-950 border border-gold-200/30 dark:border-zinc-800 rounded-xl p-3 outline-none focus:ring-1 focus:ring-gold-500 text-sm">
                                </div>
                            </div>
                            <div>
                                <label class="block text-[10px] uppercase tracking-wider text-gray-500 mb-2 font-semibold">Topic of Discussion</label>
                                <input type="text" required placeholder="Inquiry" class="w-full bg-white dark:bg-zinc-950 border border-gold-200/30 dark:border-zinc-800 rounded-xl p-3 outline-none focus:ring-1 focus:ring-gold-500 text-sm">
                            </div>
                            <div>
                                <label class="block text-[10px] uppercase tracking-wider text-gray-500 mb-2 font-semibold">Your Message</label>
                                <textarea required rows="4" placeholder="Hi Ninis..." class="w-full bg-white dark:bg-zinc-950 border border-gold-200/30 dark:border-zinc-800 rounded-xl p-3 outline-none focus:ring-1 focus:ring-gold-500 text-sm"></textarea>
                            </div>

                            <!-- Success banner -->
                            <div id="contact-success" class="hidden bg-gold-100 dark:bg-zinc-800 border border-gold-300 dark:border-zinc-700 text-gold-800 dark:text-gold-400 p-4 rounded-xl text-xs flex items-center gap-3">
                                <i class="fa-solid fa-circle-check text-lg"></i>
                                <div>
                                    <strong>Message Simulation Sent!</strong> Your simulated message was processed.
                                </div>
                            </div>

                            <button type="submit" class="w-full py-3 bg-gold-500 hover:bg-gold-600 text-apple-dark font-semibold rounded-full transition shadow-md hover:shadow-gold-500/10 flex items-center justify-center gap-2">
                                <i class="fa-solid fa-paper-plane text-xs"></i> Send Message
                            </button>
                        </form>
                    </div>
                </div>
            </section>

            <!-- Elegant Simple Footer -->
            <footer class="bg-white dark:bg-apple-dark border-t border-gold-200/20 dark:border-zinc-900 py-12 text-center text-xs text-gray-500 dark:text-gray-400 space-y-4 mt-auto">
                <p>&copy; 2026 <span class="display-fullName">Ninis Twumasi</span>. Developed for CSE Portfolios.</p>
                <div class="flex justify-center gap-4 text-xs font-medium">
                    <a href="#" onclick="navigateTo('page-about')" class="hover:text-gold-500 transition">About</a>
                    <a href="#" onclick="navigateTo('page-resume')" class="hover:text-gold-500 transition">CV Resume</a>
                    <a href="#" onclick="navigateTo('page-skills')" class="hover:text-gold-500 transition">Skills</a>
                    <a href="#" onclick="navigateTo('page-projects')" class="hover:text-gold-500 transition">Work</a>
                </div>
            </footer>
        </main>
    </div>

    <!-- 
      PROCESS: WEB WORKSPACE JAVASCRIPT LOGIC
      This script handles all dynamic changes on the webpage, such as theme changing, 
      routing, page navigation, live customizer updates, and game and visualizer logic.
    -->
    <script>
        // Dynamic backgrounds used for shuffling the homepage visually
        const backgrounds = [
            "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=1920&auto=format&fit=crop", 
            "https://images.unsplash.com/photo-1579546929518-9e396f3cc809?q=80&w=1920&auto=format&fit=crop", 
            "https://images.unsplash.com/photo-1508739773434-c26b3d09e071?q=80&w=1920&auto=format&fit=crop", 
            "https://images.unsplash.com/photo-1518770660439-4636190af475?q=80&w=1920&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1550684848-fac1c5b4e853?q=80&w=1920&auto=format&fit=crop"
        ];

        let currentBgIndex = 0;

        // Shuffle background function: Picks a random white/gold abstract image and applies it smoothly
        function shuffleBackground() {
            currentBgIndex = Math.floor(Math.random() * backgrounds.length);
            const hero = document.getElementById("page-home");
            if (hero) {
                hero.style.backgroundImage = `url('${backgrounds[currentBgIndex]}')`;
                hero.style.backgroundSize = "cover";
                hero.style.backgroundPosition = "center";
            }
        }

        // Auto shuffle the home background every 10 seconds for dynamic presentation
        setInterval(shuffleBackground, 10000);

        // Apple full screen overlay menu display controls
        function openMenuOverlay() {
            const overlay = document.getElementById('full-menu-overlay');
            overlay.classList.remove('opacity-0', 'pointer-events-none', 'scale-95');
            overlay.classList.add('opacity-100', 'scale-100');
            document.body.style.overflow = 'hidden';
        }

        function closeMenuOverlay() {
            const overlay = document.getElementById('full-menu-overlay');
            overlay.classList.add('opacity-0', 'pointer-events-none', 'scale-95');
            overlay.classList.remove('opacity-100', 'scale-100');
            document.body.style.overflow = '';
        }

        // Navigation Router: Hides all sections and activates the chosen one
        function navigateTo(pageId) {
            const pages = ['page-home', 'page-about', 'page-resume', 'page-skills', 'page-projects', 'page-contact'];
            
            pages.forEach(p => {
                const el = document.getElementById(p);
                if (el) {
                    el.classList.add('hidden');
                }
            });

            const activePage = document.getElementById(pageId);
            if (activePage) {
                activePage.classList.remove('hidden');
            }

            // Highlighting the active link in headers
            const headerLinks = document.querySelectorAll('.nav-link');
            headerLinks.forEach(link => {
                if (link.getAttribute('onclick').includes(pageId)) {
                    link.classList.add('text-gold-500', 'border-b-2', 'border-gold-500', 'pb-1');
                } else {
                    link.classList.remove('text-gold-500', 'border-b-2', 'border-gold-500', 'pb-1');
                }
            });

            closeMenuOverlay();
            window.scrollTo(0, 0);
        }

        // Skills category filtering: Hides and shows cards based on metadata category attributes
        function filterSkills(category) {
            const cards = document.querySelectorAll('.skill-card');
            const buttons = document.querySelectorAll('.filter-btn');

            buttons.forEach(btn => {
                if (btn.getAttribute('onclick').includes(category)) {
                    btn.className = "filter-btn px-5 py-2 bg-gold-500 text-apple-dark text-xs font-bold uppercase tracking-widest rounded-full transition shadow-sm";
                } else {
                    btn.className = "filter-btn px-5 py-2 bg-white dark:bg-zinc-900 border border-gold-200 dark:border-zinc-800 text-gray-600 dark:text-gray-300 text-xs font-bold uppercase tracking-widest rounded-full transition hover:border-gold-500";
                }
            });

            cards.forEach(card => {
                if (category === 'all' || card.getAttribute('data-category') === category) {
                    card.classList.remove('hidden');
                    card.classList.add('scale-100', 'opacity-100');
                } else {
                    card.classList.add('hidden');
                    card.classList.remove('scale-100', 'opacity-100');
                }
            });
        }

        // Live Customizer: Real-time syncing from input fields to target display classes
        function syncCustomizerFields() {
            const fields = ["firstName", "lastName", "academicTitle", "school", "gradeLevel", "email", "hobbies", "careerGoal"];
            
            const first = document.getElementById("input-firstName").value;
            const last = document.getElementById("input-lastName").value;
            const full = `${first} ${last}`;

            const logo = document.getElementById("nav-logo-name");
            if (logo) logo.innerText = first;

            fields.forEach(field => {
                const val = document.getElementById(`input-${field}`).value;
                document.querySelectorAll(`.display-${field}`).forEach(el => {
                    el.innerText = val;
                });
            });

            document.querySelectorAll(".display-fullName").forEach(el => {
                el.innerText = full;
            });
        }

        // Base configurations for Customizer Reset
        const defaults = {
            firstName: "Ninis",
            lastName: "Twumasi",
            academicTitle: "Sophomore & CS Student at The Browning School",
            school: "The Browning School",
            gradeLevel: "Sophomore (Class of 2028)",
            email: "ntwumasi@browning.edu",
            hobbies: "Soccer, Creative Writing, Track, Public Speaking, Community Activism",
            careerGoal: "To leverage storytelling, community engagement, and logic to drive social advocacy."
        };

        function resetToDefaults() {
            Object.keys(defaults).forEach(key => {
                const inp = document.getElementById(`input-${key}`);
                if (inp) inp.value = defaults[key];
            });
            syncCustomizerFields();
        }

        function toggleCustomizer() {
            const panel = document.getElementById('customizer');
            panel.classList.toggle('hidden');
        }

        // Theme control setting: Checks system preference or local choice
        function initTheme() {
            if (localStorage.theme === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
                document.documentElement.classList.add('dark');
            } else {
                document.documentElement.classList.remove('dark');
            }
        }

        function toggleDarkMode() {
            if (document.documentElement.classList.contains('dark')) {
                document.documentElement.classList.remove('dark');
                localStorage.theme = 'light';
            } else {
                document.documentElement.classList.add('dark');
                localStorage.theme = 'dark';
            }
        }

        // Interactive Code Compilation logic
        function executePyDemo() {
            const out = document.getElementById("py-output");
            out.innerHTML = `
                <span class="text-zinc-500">// Simulating Python Output:</span><br>
                <strong>&gt;&gt;&gt; print(Portfolio().owner)</strong><br>
                <span class="text-gold-500">"${document.getElementById("input-firstName").value} ${document.getElementById("input-lastName").value}"</span><br><br>
                <strong>&gt;&gt;&gt; print(Portfolio().academic)</strong><br>
                <span class="text-gold-500">"Sophomore at The Browning School (Class of 2028)"</span>
            `;
        }

        // --- BINARY SEARCH GUESSING GAME LOGIC ---
        let secretNumber = Math.floor(Math.random() * 20) + 1;
        let attempts = 0;
        const gameDisplay = document.getElementById('game-display');
        const gameInput = document.getElementById('game-guess-input');

        function playMiniGame() {
            const guess = parseInt(gameInput.value);
            if (isNaN(guess) || guess < 1 || guess > 20) {
                gameDisplay.textContent = "Error: Input must be a valid number between 1 and 20!";
                return;
            }
            attempts++;
            if (guess === secretNumber) {
                gameDisplay.textContent = `Correct! 🎉\nYou solved it in ${attempts} attempts.\nSecret target reset! Go again.`;
                secretNumber = Math.floor(Math.random() * 20) + 1;
                attempts = 0;
            } else if (guess < secretNumber) {
                gameDisplay.textContent = `Attempt ${attempts}: ${guess} is too low. Try higher!`;
            } else {
                gameDisplay.textContent = `Attempt ${attempts}: ${guess} is too high. Try lower!`;
            }
            gameInput.value = "";
        }

        // --- SORTING ALGORITHM SIMULATED STEP LOGIC ---
        let sortingData = [40, 70, 20, 90, 50, 10];
        const barsContainer = document.getElementById('sorting-bars');
        const sortStatus = document.getElementById('sorting-status');

        function renderSortingBars() {
            barsContainer.innerHTML = '';
            sortingData.forEach(val => {
                const bar = document.createElement('div');
                bar.style.height = `${val}%`;
                bar.className = "bg-gold-500 w-full rounded-t transition-all duration-300 relative group flex items-end justify-center";
                barsContainer.appendChild(bar);
            });
        }

        function startBubbleSortSim() {
            sortStatus.textContent = "Processing logic...";
            sortStatus.className = "text-[10px] text-gold-500 font-mono animate-pulse";
            
            // Traditional sorting pass comparison
            for (let i = 0; i < sortingData.length - 1; i++) {
                if (sortingData[i] > sortingData[i+1]) {
                    let temp = sortingData[i];
                    sortingData[i] = sortingData[i+1];
                    sortingData[i+1] = temp;
                    renderSortingBars();
                    break;
                }
            }
            setTimeout(() => {
                sortStatus.textContent = "Step completed!";
                sortStatus.className = "text-[10px] text-green-500 font-mono";
            }, 300);
        }

        // Form submission simulation
        function handleContactSubmit(event) {
            event.preventDefault();
            const success = document.getElementById('contact-success');
            success.classList.remove('hidden');
            event.target.reset();
            setTimeout(() => { success.classList.add('hidden'); }, 5000);
        }

        // Initial launch parameters
        window.onload = function() {
            initTheme();
            renderSortingBars();
            shuffleBackground();
            syncCustomizerFields();
        };
    </script>
</body>
</html>