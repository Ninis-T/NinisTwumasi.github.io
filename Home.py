<!-- 
==================================================================
NINIS TWUMASI - THE BROWNING SCHOOL PORTFOLIO
==================================================================
* Theme: Premium Gold, Dark Black, and Alabaster White
* Style: Apple Minimalist Aesthetic
* Host Compatibility: GitHub Pages (Single-file index.html)
==================================================================
-->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ninis Twumasi | Sophomore Portfolio</title>
    
    <!-- 
      PROCESS: STYLING & DESIGN ARCHITECTURE
      We import Tailwind CSS to build an ultra-clean, elegant design directly 
      within our HTML class tags. We configure custom 'gold' and 'apple' 
      design colors to match Apple's modern minimalist color palette.
    -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    colors: {
                        gold: {
                            50: '#FDFBF7',   // Warm alabaster backdrop
                            100: '#F9F6EE',  // Soft white satin
                            200: '#F3E9CE',  // Champagne gold sand
                            300: '#EADAA9',  // Gold satin highlight
                            500: '#D4AF37',  // Metallic gold leaf
                            600: '#C5A028',  // Burnished satin gold
                            700: '#A3801A',  // Classic gold border
                            900: '#4E3E12',  // Dark gold bronze
                            950: '#1C1605',  // Dark golden obsidian
                        },
                        apple: {
                            gray: '#F5F5F7', // Apple signature gray
                            dark: '#08080A', // Deep black backing
                            zinc: '#121215', // Premium dark card containers
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

    <!-- FontAwesome: Used to load high-quality vector icons for academic, leadership, and athletic categories -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- Google Fonts: Playfair Display for headers and Inter for clean, readable body paragraphs -->
    <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;600&family=Inter:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&swap" rel="stylesheet">

    <!-- 
      PROCESS: LAYOUT TRANSITIONS & CUSTOM PRINT STYLING
      * Smooth transitions make background image shuffling feel highly polished.
      * Media Print Stylesheet optimizes your layout when printing or saving as a PDF 
        by hiding navigation links, button controls, and footer blocks.
    -->
    <style>
        html {
            scroll-behavior: smooth;
        }
        /* Fluid transitions for shuffling background images */
        .bg-transition {
            transition: background-image 1.2s ease-in-out, background-color 0.8s ease-in-out;
        }
        /* Custom sleek golden scrollbars */
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
        /* Ambient golden glow effect for showcase items */
        .gold-glow {
            box-shadow: 0 0 20px rgba(212, 175, 55, 0.15);
        }
        .gold-glow:hover {
            box-shadow: 0 0 30px rgba(212, 175, 55, 0.35);
        }

        /* Standardized Print/PDF output configurations */
        @media print {
            body {
                background: white !important;
                color: black !important;
            }
            header, footer, .filter-btn, .no-print, #menu-overlay-button {
                display: none !important;
            }
            .page-container {
                display: block !important;
                opacity: 1 !important;
            }
            .print-full-width {
                width: 100% !important;
                max-width: 100% !important;
            }
        }
    </style>
</head>
<body class="bg-gold-50 text-gray-900 dark:bg-apple-dark dark:text-gray-100 font-sans transition-colors duration-300 min-h-screen flex flex-col overflow-x-hidden">

    <!-- Main Workspace Container -->
    <div class="flex flex-1 relative print-full-width">
        <main class="flex-1 flex flex-col min-h-screen print-full-width">
            
            <!-- 
              PROCESS: APPLE GLASS NAVIGATION HEADER
              A sleek frosted glass navigation header that stays sticky at the top 
              of the viewport and allows users to jump between sections instantly.
            -->
            <header class="bg-white/90 dark:bg-apple-dark/90 backdrop-blur-md border-b border-gold-200/20 dark:border-zinc-900 sticky top-0 z-30 transition-colors no-print">
                <div class="max-w-6xl mx-auto px-6 py-4 flex justify-between items-center">
                    <a href="#" onclick="navigateTo('page-home')" class="flex items-center gap-2 font-bold text-lg tracking-tight hover:opacity-85 transition text-gold-600 dark:text-gold-400">
                        <span class="font-light text-gray-400">&lt;</span><span>Ninis</span><span class="font-light text-gray-400">.js /&gt;</span>
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

                        <!-- Theme & Menu Toggle Buttons -->
                        <div class="flex items-center gap-3 border-l border-gold-200/30 pl-4">
                            <!-- Premium Light / Dark mode toggle switch -->
                            <button onclick="toggleDarkMode()" class="text-gray-400 hover:text-gold-500 p-2 rounded-full hover:bg-gold-100/30 transition">
                                <i class="fa-solid fa-moon dark:hidden"></i>
                                <i class="fa-solid fa-sun hidden dark:inline"></i>
                            </button>
                            <!-- Apple Full Screen minimalist menu button -->
                            <button id="menu-overlay-button" onclick="openMenuOverlay()" class="text-gray-700 dark:text-gray-200 hover:text-gold-500 p-2 rounded-full hover:bg-gold-100/30 transition flex items-center gap-1.5">
                                <span class="text-[10px] font-bold tracking-widest uppercase hidden sm:inline">Menu</span>
                                <i class="fa-solid fa-bars-staggered text-lg"></i>
                            </button>
                        </div>
                    </div>
                </div>
            </header>

            <!-- 
              PROCESS: FULL-PAGE OVERLAY MENU
              Covers the page it is on with a sleek blurred glass backdrop. 
              Provides a beautiful navigation experience.
            -->
            <div id="full-menu-overlay" class="fixed inset-0 bg-white/98 dark:bg-apple-dark/98 backdrop-blur-2xl z-50 flex flex-col justify-between p-8 transition-all duration-500 opacity-0 pointer-events-none scale-95 no-print">
                <div class="flex justify-between items-center max-w-6xl w-full mx-auto">
                    <span class="font-bold text-xl tracking-tight text-gold-600 dark:text-gold-400 font-mono">&lt;Ninis.js /&gt;</span>
                    <button onclick="closeMenuOverlay()" class="w-12 h-12 rounded-full border border-gold-200/50 dark:border-zinc-850 flex items-center justify-center text-gray-500 hover:text-gold-500 dark:hover:text-gold-400 transition hover:rotate-90">
                        <i class="fa-solid fa-xmark text-lg"></i>
                    </button>
                </div>

                <!-- Vertical navigation list inside overlay -->
                <nav class="flex flex-col items-center justify-center space-y-6 text-center my-auto font-sans">
                    <span class="text-[11px] font-bold text-gold-500 uppercase tracking-widest mb-2">Select Page Module</span>
                    <a href="#" onclick="navigateTo('page-home')" class="text-4xl sm:text-6xl font-serif font-light text-gray-800 dark:text-gray-100 hover:text-gold-500 transition tracking-tight">01 / Home</a>
                    <a href="#" onclick="navigateTo('page-about')" class="text-4xl sm:text-6xl font-serif font-light text-gray-800 dark:text-gray-100 hover:text-gold-500 transition tracking-tight">02 / About Me</a>
                    <a href="#" onclick="navigateTo('page-resume')" class="text-4xl sm:text-6xl font-serif font-light text-gray-800 dark:text-gray-100 hover:text-gold-500 transition tracking-tight">03 / Academic Resume</a>
                    <a href="#" onclick="navigateTo('page-skills')" class="text-4xl sm:text-6xl font-serif font-light text-gray-800 dark:text-gray-100 hover:text-gold-500 transition tracking-tight">04 / Core Skills</a>
                    <a href="#" onclick="navigateTo('page-projects')" class="text-4xl sm:text-6xl font-serif font-light text-gray-800 dark:text-gray-100 hover:text-gold-500 transition tracking-tight">05 / Projects &amp; Games</a>
                    <a href="#" onclick="navigateTo('page-contact')" class="text-4xl sm:text-6xl font-serif font-light text-gray-800 dark:text-gray-100 hover:text-gold-500 transition tracking-tight">06 / Contact Hub</a>
                </nav>

                <div class="text-center text-xs text-gray-400 max-w-xl mx-auto space-y-2 font-sans">
                    <p class="font-mono text-gold-600">Pure HTML, CSS, and JS. Ready for GitHub Pages.</p>
                    <p>&copy; 2026 Ninis. All Rights Reserved.</p>
                </div>
            </div>

            <!-- PAGE 1: HOME PAGE (Active by default) -->
            <section id="page-home" class="page-container flex-1 bg-transition relative flex items-center py-16 md:py-28 min-h-[85vh] bg-gold-50 dark:bg-apple-dark">
                
                <!-- Glowing Golden "NT" Monogram Overlay (Option 4 is black background with gold "NT") -->
                <div id="nt-monogram-bg" class="absolute inset-0 bg-black flex flex-col items-center justify-center pointer-events-none opacity-0 transition-opacity duration-1000 no-print z-0">
                    <div class="w-48 h-48 rounded-full border border-gold-500/20 flex items-center justify-center shadow-[0_0_50px_rgba(212,175,55,0.1)]">
                        <span class="font-serif font-light text-7xl tracking-widest text-transparent bg-clip-text bg-gradient-to-r from-gold-300 via-gold-500 to-gold-600 drop-shadow-[0_0_15px_rgba(212,175,55,0.4)]">NT</span>
                    </div>
                    <span class="text-[10px] text-gold-500/60 font-mono tracking-[0.25em] uppercase mt-4">Ninis Twumasi Portfolio</span>
                </div>

                <!-- Inner Content Container -->
                <div class="max-w-6xl mx-auto px-6 w-full grid grid-cols-1 lg:grid-cols-12 gap-12 items-center relative z-10">
                    
                    <!-- Hero Information Text -->
                    <div class="lg:col-span-7 space-y-6" id="hero-text-block">
                        <div class="inline-flex items-center gap-2 bg-white/90 dark:bg-gold-950/20 text-gold-700 dark:text-gold-400 px-4 py-1.5 rounded-full text-[10px] font-bold uppercase tracking-widest border border-gold-200/50">
                            <span class="w-2 h-2 rounded-full bg-gold-500 animate-pulse"></span>
                            Browning Sophomore
                        </div>
                        <h1 class="text-5xl sm:text-7xl font-serif font-light tracking-tight leading-none text-gray-900 dark:text-white">
                            Hi, I am <br><span class="font-bold text-transparent bg-clip-text bg-gradient-to-r from-gold-500 to-gold-700">Ninis</span> Twumasi
                        </h1>
                        <p class="text-lg md:text-xl text-gray-700 dark:text-gray-300 font-light tracking-wide">
                            Sophomore &amp; CS Student at The Browning School
                        </p>
                        <p class="text-gray-600 dark:text-gray-400 leading-relaxed max-w-xl text-sm font-light">
                            Welcome to my personal archive. This platform represents who I am, a 15-year-old student from Manhattan, NYC, doing my best to make an impact both in and out of the classroom.
                        </p>
                        
                        <!-- Hero Actions -->
                        <div class="flex flex-wrap gap-4 pt-4 no-print">
                            <button onclick="navigateTo('page-about')" class="px-8 py-3.5 bg-gold-500 hover:bg-gold-600 text-apple-dark text-xs font-bold uppercase tracking-wider rounded-full shadow-lg hover:shadow-gold-500/20 transition flex items-center gap-2 font-sans">
                                Explore About Me <i class="fa-solid fa-arrow-right"></i>
                            </button>
                            <button onclick="shuffleBackground()" class="px-6 py-3.5 bg-white/90 dark:bg-zinc-900/90 backdrop-blur text-gold-600 dark:text-gold-400 border border-gold-200 dark:border-zinc-800 hover:border-gold-500 text-xs font-bold uppercase tracking-wider rounded-full transition flex items-center gap-2 shadow-sm font-sans">
                                <i class="fa-solid fa-wand-magic-sparkles animate-spin-slow"></i> Shuffle Background
                            </button>
                        </div>
                    </div>

                    <!-- Right Portrait Picture Frame -->
                    <div class="lg:col-span-5 w-full flex justify-center z-10" id="hero-image-block">
                        <div class="relative group max-w-sm w-full">
                            <div class="absolute -inset-1.5 bg-gradient-to-tr from-gold-400 via-gold-200 to-white rounded-3xl blur opacity-30 group-hover:opacity-45 transition duration-1000"></div>
                            <div class="relative bg-white dark:bg-zinc-950 p-3 rounded-3xl border border-gold-200/30 dark:border-zinc-800/80 shadow-2xl">
                                <div class="aspect-square w-full rounded-2xl overflow-hidden bg-gold-100/50 dark:bg-zinc-900 relative">
                                    <!-- Displays Ninis' uploaded image -->
                                    <img src="IMG_0594 Small.jpeg" alt="Ninis Twumasi Portrait" class="w-full h-full object-cover" onerror="this.style.display='none'; this.nextElementSibling.classList.remove('hidden')">
                                    <!-- Fallback design icon if local file isn't loaded -->
                                    <div class="hidden absolute inset-0 flex items-center justify-center bg-zinc-900">
                                        <i class="fa-solid fa-user-tie text-gold-500 text-6xl"></i>
                                    </div>
                                    <div class="absolute bottom-4 left-4 right-4 bg-black/70 backdrop-blur-md rounded-xl p-3 border border-white/10 text-white text-xs font-sans">
                                        <p class="font-semibold tracking-wide text-gold-400 text-xs">The Browning School</p>
                                        <p class="text-[10px] text-zinc-300 font-mono mt-0.5">Manhattan, NYC</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- PAGE 2: ABOUT ME -->
            <section id="page-about" class="page-container flex-1 py-20 bg-white dark:bg-apple-dark transition-colors hidden">
                <div class="max-w-6xl mx-auto px-6">
                    <div class="text-center max-w-2xl mx-auto mb-16">
                        <span class="text-[10px] font-bold text-gold-500 uppercase tracking-widest">About the Programmer</span>
                        <h2 class="text-4xl font-serif font-light tracking-tight text-gray-900 dark:text-white mt-2">Ninis Twumasi</h2>
                        <div class="w-12 h-[2px] bg-gold-400 mx-auto rounded mt-3"></div>
                    </div>

                    <div class="grid grid-cols-1 md:grid-cols-12 gap-12 items-center">
                        <!-- Left Image Frame -->
                        <div class="md:col-span-5 flex flex-col items-center">
                            <div class="relative group w-full max-w-xs">
                                <div class="absolute -inset-1 bg-gradient-to-r from-gold-300 to-gold-600 rounded-2xl blur opacity-35 transition duration-1000"></div>
                                <div class="relative bg-white dark:bg-zinc-900 p-2 rounded-2xl border border-gold-200/50 dark:border-zinc-800">
                                    <div class="aspect-square w-full bg-gold-100/50 dark:bg-zinc-850 rounded-xl overflow-hidden relative">
                                        <img src="IMG_1053 Small.jpeg" alt="Ninis Twumasi Portrait" class="w-full h-full object-cover" onerror="this.style.display='none'; this.nextElementSibling.classList.remove('hidden')">
                                        <div class="hidden absolute inset-0 flex items-center justify-center bg-zinc-905">
                                            <i class="fa-solid fa-graduation-cap text-gold-500 text-5xl"></i>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Right Biography details -->
                        <div class="md:col-span-7 space-y-6">
                            <h3 class="text-2xl font-serif font-light text-gray-800 dark:text-gray-200 tracking-wide">
                                Manhattan Student &amp; Community Advocate
                            </h3>
                            <p class="text-gray-600 dark:text-gray-300 leading-relaxed font-light text-sm">
                                Welcome to My Website! This website is coded 100% by me and is a reflection of who I am, a 15-year-old student from Manhattan, NYC, doing my best to make an impact both in and out of the classroom. I'm currently a sophomore at The Browning School, where I stay busy between classes, soccer, track, and everything in between. Community is at the core of who I am. When asked about me in a few words to describe me, I am called kind-hearted, charismatic, persistent, driven, and determined. Whenever I am motivated about something, I always see it through. In addition, whenever someone needs me, I am always there for them.
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
                                    <p class="text-xs text-gray-500 dark:text-gray-400 leading-relaxed font-light">
                                        Soccer, Creative Writing, Track, Public Speaking, Community Activism
                                    </p>
                                </div>
                                <div>
                                    <h4 class="font-semibold text-xs uppercase tracking-wider text-gold-600 dark:text-gold-400 flex items-center gap-2 mb-2">
                                        <i class="fa-solid fa-bullseye"></i> Core Career Goal
                                    </h4>
                                    <p class="text-xs text-gray-500 dark:text-gray-400 leading-relaxed font-light">
                                        To leverage storytelling, community engagement, and logic to drive social advocacy.
                                    </p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- PAGE 3: RESUME PAGE -->
            <section id="page-resume" class="page-container flex-1 py-20 bg-gold-100/30 dark:bg-apple-dark/60 transition-colors hidden">
                <div class="max-w-6xl mx-auto px-6">
                    <div class="text-center max-w-2xl mx-auto mb-12">
                        <span class="text-[10px] font-bold text-gold-500 uppercase tracking-widest">Academic & Activity Curriculum</span>
                        <h2 class="text-4xl font-serif font-light tracking-tight text-gray-900 dark:text-white mt-2">Resume & Experience</h2>
                        <div class="w-12 h-[2px] bg-gold-400 mx-auto rounded mt-3"></div>
                        <p class="text-sm text-gray-400 mt-2">Sophomore at The Browning School, Dedicated to academic excellence and leadership.</p>
                        
                        <!-- Print styling trigger button for keeping a PDF form -->
                        <div class="mt-6 flex justify-center no-print">
                            <button onclick="window.print()" class="px-6 py-2.5 bg-gold-500 hover:bg-gold-600 text-apple-dark font-semibold text-xs rounded-full uppercase tracking-wider shadow-md transition duration-300 flex items-center gap-2 font-sans">
                                <i class="fa-solid fa-file-pdf"></i> Keep / Save PDF Resume
                            </button>
                        </div>
                    </div>

                    <!-- Highlighted Group Spotlight: Black Student Coalition NYC Representative -->
                    <div class="mb-12 bg-white dark:bg-apple-zinc border border-gold-200/40 dark:border-zinc-800 rounded-3xl p-6 lg:p-8 grid grid-cols-1 md:grid-cols-12 gap-8 items-center">
                        <div class="md:col-span-5 rounded-2xl overflow-hidden relative shadow-md aspect-[4/3] bg-zinc-900">
                            <!-- Group image source configured with user uploaded file -->
                            <img src="IMG_1936.jpg" alt="Black Student Coalition NYC group" class="w-full h-full object-cover" onerror="this.style.display='none'; this.nextElementSibling.classList.remove('hidden')">
                            <div class="hidden absolute inset-0 flex items-center justify-center bg-zinc-900 text-gold-500">
                                <i class="fa-solid fa-users text-5xl"></i>
                            </div>
                        </div>
                        <div class="md:col-span-7 space-y-4 font-sans">
                            <span class="inline-block bg-gold-100 dark:bg-gold-950/40 text-gold-700 dark:text-gold-400 text-[9px] font-bold uppercase tracking-widest px-3 py-1 rounded-full border border-gold-200/20">Featured Coalition Spotlight</span>
                            <h3 class="text-xl font-serif font-semibold text-gray-900 dark:text-white">Black Student Coalition NYC Representative</h3>
                            <p class="text-xs text-gray-500 dark:text-zinc-400 leading-relaxed font-light">
                                Serve as Browning’s representative to the Black Student Coalition NYC, an organization connecting Black students across New York City. Promote Black culture, encourage meaningful discussions, and help build a supportive and empowering community among students.
                            </p>
                        </div>
                    </div>

                    <div class="grid grid-cols-1 lg:grid-cols-12 gap-8">
                        <!-- Left Timeline -->
                        <div class="lg:col-span-8 space-y-8">
                            <div class="bg-white dark:bg-apple-zinc p-8 rounded-2xl shadow-sm border border-gold-200/30 dark:border-zinc-850">
                                <h3 class="font-serif font-bold text-lg text-gold-600 dark:text-gold-400 border-b border-gold-100 dark:border-zinc-800 pb-3 mb-6 flex items-center gap-2">
                                    <i class="fa-solid fa-scroll text-sm"></i> Leadership &amp; Clubs
                                </h3>

                                <div class="relative border-l-2 border-gold-200 dark:border-zinc-800 ml-2 pl-6 space-y-8 font-sans">
                                    <!-- JV Soccer Captain -->
                                    <div class="relative animate-fade-in">
                                        <span class="absolute -left-[31px] top-1.5 bg-gold-500 w-4 h-4 rounded-full border-4 border-white dark:border-apple-zinc"></span>
                                        <span class="text-[10px] font-mono font-bold text-gold-600 dark:text-gold-400 uppercase tracking-widest">2025</span>
                                        <h4 class="font-semibold text-sm text-gray-900 dark:text-white mt-1">Soccer JV Captain</h4>
                                        <p class="text-xs text-gray-500 dark:text-zinc-400 mt-1 leading-relaxed">
                                            I played competitive soccer for over six years, developing strong teamwork, communication, and leadership skills. Served as JV Captain, helping lead practices, motivate teammates, and promote collaboration on and off the field.
                                        </p>
                                    </div>

                                    <!-- Browning Food Recovery Program -->
                                    <div class="relative">
                                        <span class="absolute -left-[31px] top-1.5 bg-gold-500 w-4 h-4 rounded-full border-4 border-white dark:border-apple-zinc"></span>
                                        <span class="text-[10px] font-mono font-bold text-gold-600 dark:text-gold-400 uppercase tracking-widest">Founder</span>
                                        <h4 class="font-semibold text-sm text-gray-900 dark:text-white mt-1">Founder, Browning Food Recovery Program with Grassroots Grocery</h4>
                                        <p class="text-xs text-gray-500 dark:text-zinc-400 mt-1 leading-relaxed">
                                            Founded Browning’s Food Recovery Program in partnership with Grassroots Grocery to help combat food insecurity. Worked to redirect unused resources toward supporting communities in need and promoting service within the Browning community.
                                        </p>
                                    </div>

                                    <!-- Chief Editor -->
                                    <div class="relative">
                                        <span class="absolute -left-[31px] top-1.5 bg-gold-500 w-4 h-4 rounded-full border-4 border-white dark:border-apple-zinc"></span>
                                        <span class="text-[10px] font-mono font-bold text-gold-600 dark:text-gold-400 uppercase tracking-widest">2021 – 2024</span>
                                        <h4 class="font-semibold text-sm text-gray-900 dark:text-white mt-1">Chief Editor, Middle School Newspaper</h4>
                                        <p class="text-xs text-gray-500 dark:text-zinc-400 mt-1 leading-relaxed">
                                            Founded and led Browning’s Middle School newspaper out of a passion for storytelling and sharing information with the community. Oversaw article creation, editing, and publication while encouraging student voices and school engagement.
                                        </p>
                                    </div>

                                    <!-- All-School Green Team -->
                                    <div class="relative">
                                        <span class="absolute -left-[31px] top-1.5 bg-gold-500 w-4 h-4 rounded-full border-4 border-white dark:border-apple-zinc"></span>
                                        <span class="text-[10px] font-mono font-bold text-gold-600 dark:text-gold-400 uppercase tracking-widest">2022 – 2024</span>
                                        <h4 class="font-semibold text-sm text-gray-900 dark:text-white mt-1">All-School Green Team Leadership</h4>
                                        <p class="text-xs text-gray-500 dark:text-zinc-400 mt-1 leading-relaxed">
                                            Helped lead environmental initiatives aimed at making Browning a more sustainable and environmentally conscious community. Organized fundraisers and promoted projects focused on environmental awareness and positive change within the school.
                                        </p>
                                    </div>

                                    <!-- Class Representative -->
                                    <div class="relative">
                                        <span class="absolute -left-[31px] top-1.5 bg-gold-500 w-4 h-4 rounded-full border-4 border-white dark:border-apple-zinc"></span>
                                        <span class="text-[10px] font-mono font-bold text-gold-600 dark:text-gold-400 uppercase tracking-widest">2025</span>
                                        <h4 class="font-semibold text-sm text-gray-900 dark:text-white mt-1">Class Representative</h4>
                                        <p class="text-xs text-gray-500 dark:text-zinc-400 mt-1 leading-relaxed">
                                            Represented my grade by advocating for student voices and communicating student concerns and ideas. Strengthened my leadership, public speaking, and self-advocacy skills while learning how to handle feedback and rejection constructively.
                                        </p>
                                    </div>

                                    <!-- Student Council -->
                                    <div class="relative">
                                        <span class="absolute -left-[31px] top-1.5 bg-gold-500 w-4 h-4 rounded-full border-4 border-white dark:border-apple-zinc"></span>
                                        <span class="text-[10px] font-mono font-bold text-gold-600 dark:text-gold-400 uppercase tracking-widest">2021 – 2024</span>
                                        <h4 class="font-semibold text-sm text-gray-900 dark:text-white mt-1">Middle School Student Council</h4>
                                        <p class="text-xs text-gray-500 dark:text-zinc-400 mt-1 leading-relaxed">
                                            Participated in Student Council to help represent the middle school community and contribute to school improvement efforts. Assisted with community service initiatives, student events, and projects designed to strengthen school spirit and engagement.
                                        </p>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Right Column Timelines -->
                        <div class="lg:col-span-4 space-y-6">
                            <!-- Education Card -->
                            <div class="bg-white dark:bg-apple-zinc p-6 rounded-2xl shadow-sm border border-gold-200/30 dark:border-zinc-850">
                                <h3 class="font-serif font-bold text-base text-gold-600 dark:text-gold-400 border-b border-gold-100 dark:border-zinc-800 pb-2 mb-4 flex items-center gap-2">
                                    <i class="fa-solid fa-graduation-cap"></i> Education
                                </h3>
                                <div class="relative pl-4 border-l-2 border-gold-500 py-1">
                                    <h4 class="font-semibold text-sm">The Browning School</h4>
                                    <p class="text-xs text-gray-400 font-mono">Sophomore (Class of 2028)</p>
                                    <p class="text-xs text-gray-500 mt-1">Browning Enrollment: 2021–2026</p>
                                </div>
                            </div>

                            <!-- Summer Counselor Job Card -->
                            <div class="bg-white dark:bg-apple-zinc p-6 rounded-2xl shadow-sm border border-gold-200/30 dark:border-zinc-850">
                                <h3 class="font-serif font-bold text-base text-gold-600 dark:text-gold-400 border-b border-gold-100 dark:border-zinc-800 pb-2 mb-4 flex items-center gap-2">
                                    <i class="fa-solid fa-briefcase"></i> Experience
                                </h3>
                                <div class="relative pl-4 border-l-2 border-gold-500 py-1">
                                    <h4 class="font-semibold text-sm">Camp Counselor</h4>
                                    <p class="text-xs text-gray-500 font-mono font-bold">Camp KenMont and KenWood</p>
                                    <p class="text-xs text-gray-400 font-mono">Summer 2026</p>
                                    <p class="text-xs text-gray-400 mt-2 leading-relaxed text-xs">
                                        I will be serving as a Camp Counselor at Camp KenMont and KenWood from July 19th to August 16th. Having attended the camp for the past two years, I look forward to giving back to the community that has positively impacted me. This experience will allow me to develop leadership, responsibility, and mentorship skills while working closely with children in a team-oriented environment.
                                    </p>
                                </div>
                            </div>

                            <!-- Academic Pursuits and Clubs Card -->
                            <div class="bg-white dark:bg-apple-zinc p-6 rounded-2xl shadow-sm border border-gold-200/30 dark:border-zinc-850">
                                <h3 class="font-serif font-bold text-base text-gold-600 dark:text-gold-400 border-b border-gold-100 dark:border-zinc-800 pb-2 mb-4 flex items-center gap-2">
                                    <i class="fa-solid fa-bookmark"></i> Academic Clubs
                                </h3>
                                <ul class="space-y-4 text-xs font-sans">
                                    <li class="border-b border-gold-100 dark:border-zinc-800 pb-2 last:border-b-0 last:pb-0">
                                        <p class="font-semibold text-gray-900 dark:text-white text-xs">Time for Kids Reporter (2023–2024)</p>
                                        <p class="text-gray-400 mt-0.5">Contributed articles focused on current events and topics I am passionate about in order to spread awareness and inform readers. Strengthened my writing, journalism, and communication skills.</p>
                                    </li>
                                    <li class="border-b border-gold-100 dark:border-zinc-800 pb-2 last:border-b-0 last:pb-0">
                                        <p class="font-semibold text-gray-900 dark:text-white text-xs">Mock Trial (2023–2026)</p>
                                        <p class="text-gray-400 mt-0.5">Participated in Browning’s Mock Trial program, developing skills in public speaking, reasoning, advocacy, and critical thinking under pressure.</p>
                                    </li>
                                    <li class="border-b border-gold-100 dark:border-zinc-800 pb-2 last:border-b-0 last:pb-0">
                                        <p class="font-semibold text-gray-900 dark:text-white text-xs">Debate Team (2024–2026)</p>
                                        <p class="text-gray-400 mt-0.5">Competed in debates focused on argumentation, public speaking, and analytical reasoning. Improved my ability to think critically and communicate effectively.</p>
                                    </li>
                                    <li class="border-b border-gold-100 dark:border-zinc-800 pb-2 last:border-b-0 last:pb-0">
                                        <p class="font-semibold text-gray-900 dark:text-white text-xs">Urban Barcoding (2024–2025)</p>
                                        <p class="text-gray-400 mt-0.5">Participated in scientific research focused on biodiversity and environmental science through urban barcoding projects.</p>
                                    </li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- PAGE 4: SKILLS PAGE -->
            <section id="page-skills" class="page-container flex-1 py-20 bg-white dark:bg-apple-dark transition-colors hidden">
                <div class="max-w-6xl mx-auto px-6">
                    <div class="text-center max-w-2xl mx-auto mb-12">
                        <span class="text-[10px] font-bold text-gold-500 uppercase tracking-widest">Skill Metrics</span>
                        <h2 class="text-4xl font-serif font-light tracking-tight text-gray-900 dark:text-white mt-2">Competencies &amp; Abilities</h2>
                        <div class="w-12 h-[2px] bg-gold-400 mx-auto rounded mt-3"></div>
                    </div>

                    <!-- Interactive Skill Filters -->
                    <div class="flex justify-center gap-3 mb-12 flex-wrap no-print font-sans">
                        <button onclick="filterSkills('all')" class="filter-btn px-5 py-2 bg-gold-500 text-apple-dark text-xs font-bold uppercase tracking-widest rounded-full transition shadow-sm">All</button>
                        <button onclick="filterSkills('tech')" class="filter-btn px-5 py-2 bg-white dark:bg-zinc-900 border border-gold-200 dark:border-zinc-800 text-gray-600 dark:text-gray-300 text-xs font-bold uppercase tracking-widest rounded-full transition hover:border-gold-500">Tech &amp; Creative</button>
                        <button onclick="filterSkills('academic')" class="filter-btn px-5 py-2 bg-white dark:bg-zinc-900 border border-gold-200 dark:border-zinc-800 text-gray-600 dark:text-gray-300 text-xs font-bold uppercase tracking-widest rounded-full transition hover:border-gold-500">Academic &amp; Speaking</button>
                        <button onclick="filterSkills('personal')" class="filter-btn px-5 py-2 bg-white dark:bg-zinc-900 border border-gold-200 dark:border-zinc-800 text-gray-600 dark:text-gray-300 text-xs font-bold uppercase tracking-widest rounded-full transition hover:border-gold-500">Leadership</button>
                    </div>

                    <div class="grid grid-cols-1 md:grid-cols-3 gap-8" id="skills-grid">
                        <!-- Tech / Creative Skills -->
                        <div class="skill-card bg-gold-100/20 dark:bg-zinc-900/40 p-8 rounded-2xl border border-gold-200/20 dark:border-zinc-850 space-y-4 transition-all duration-300 animate-fade-in" data-category="tech">
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
                        <div class="skill-card bg-gold-100/20 dark:bg-zinc-900/40 p-8 rounded-2xl border border-gold-200/20 dark:border-zinc-850 space-y-4 transition-all duration-300 animate-fade-in" data-category="academic">
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
                        <div class="skill-card bg-gold-100/20 dark:bg-zinc-900/40 p-8 rounded-2xl border border-gold-200/20 dark:border-zinc-850 space-y-4 transition-all duration-300 animate-fade-in" data-category="personal">
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

            <!-- PAGE 5: PROJECTS PAGE -->
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
                            <div class="p-4 bg-gold-100/10 dark:bg-zinc-950/40 border-t border-gold-200/20 dark:border-zinc-800 no-print">
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

                            <div class="p-4 bg-gold-100/10 dark:bg-zinc-950/40 border-t border-gold-200/20 dark:border-zinc-800 no-print">
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

            <!-- PAGE 6: CONTACT PAGE -->
            <section id="page-contact" class="page-container flex-1 py-20 bg-white dark:bg-apple-dark transition-colors hidden">
                <div class="max-w-4xl mx-auto px-6">
                    <div class="text-center max-w-2xl mx-auto mb-16">
                        <span class="text-[10px] font-bold text-gold-500 uppercase tracking-widest">Connect with me</span>
                        <h2 class="text-4xl font-serif font-light tracking-tight text-gray-900 dark:text-white mt-2">Get in Touch</h2>
                        <div class="w-12 h-[2px] bg-gold-400 mx-auto rounded mt-3"></div>
                        <p class="text-sm text-gray-400 mt-2">Have a question or want to connect? Feel free to reach out.</p>
                    </div>

                    <div class="grid grid-cols-1 md:grid-cols-3 gap-8 mb-12 font-sans">
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

                    <div class="bg-gold-50 dark:bg-apple-zinc rounded-2xl p-8 border border-gold-200/30 dark:border-zinc-850 no-print">
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

                            <button type="submit" class="w-full py-3 bg-gold-500 hover:bg-gold-600 text-apple-dark font-semibold rounded-full transition shadow-md hover:shadow-gold-500/10 flex items-center justify-center gap-2 font-sans">
                                <i class="fa-solid fa-paper-plane text-xs"></i> Send Message
                            </button>
                        </form>
                    </div>
                </div>
            </section>

            <!-- Elegant Simple Footer -->
            <footer class="bg-white dark:bg-apple-dark border-t border-gold-200/20 dark:border-zinc-900 py-12 text-center text-xs text-gray-500 dark:text-gray-400 space-y-4 mt-auto no-print">
                <p>&copy; 2026 <span>Ninis Twumasi</span>. Developed for CSE Portfolios.</p>
                <div class="flex justify-center gap-4 text-xs font-medium font-sans">
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
      routing, page navigation, and game and visualizer logic.
    -->
    <script>
        // Array of background styling configurations:
        // Config 0: IMG_1327.jpg
        // Config 1: IMG_1053 Small.jpeg
        // Config 2: IMG_0594 Small.jpeg
        // Config 3: Glowing gold "NT" monogram on a black background
        const backgrounds = [
            "url('IMG_1327.jpg')", 
            "url('IMG_1053%20Small.jpeg')", 
            "url('IMG_0594%20Small.jpeg')",
            "none"
        ];

        // Backup high-quality Unsplash gold & white marble textures in case local files fail to load in sandboxed previews
        const fallbacks = [
            "url('https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=1920')",
            "url('https://images.unsplash.com/photo-1508739773434-c26b3d09e071?q=80&w=1920')",
            "url('https://images.unsplash.com/photo-1550684848-fac1c5b4e853?q=80&w=1920')"
        ];

        let currentBgIndex = 0;

        // Shuffle background function: cycles through your custom images and custom designed black-and-gold screen
        function shuffleBackground() {
            const hero = document.getElementById("page-home");
            const ntBg = document.getElementById("nt-monogram-bg");
            const heroTextBlock = document.getElementById("hero-text-block");
            const heroImageBlock = document.getElementById("hero-image-block");
            
            if (hero && ntBg) {
                // If it is option index 3 (the custom NT Monogram black background)
                if (currentBgIndex === 3) {
                    hero.style.backgroundImage = "none";
                    hero.style.backgroundColor = "#000000";
                    ntBg.classList.remove("opacity-0");
                    ntBg.classList.add("opacity-100");
                    
                    // Style hero text block for ultra high contrast on black background
                    if (heroTextBlock) {
                        heroTextBlock.className = "lg:col-span-7 space-y-6 bg-black/60 p-8 rounded-3xl backdrop-blur-md border border-white/10 shadow-2xl relative z-10 transition-all duration-500";
                    }
                } else {
                    // Hide the golden monogram overlay
                    ntBg.classList.add("opacity-0");
                    ntBg.classList.remove("opacity-100");
                    
                    // Reset text block back to elegant simple styling
                    if (heroTextBlock) {
                        heroTextBlock.className = "lg:col-span-7 space-y-6 transition-all duration-500 relative z-10";
                    }
                    
                    // Apply image backgrounds
                    hero.style.backgroundImage = backgrounds[currentBgIndex];
                    hero.style.backgroundSize = "cover";
                    hero.style.backgroundPosition = "center";
                    
                    // Verify if local image successfully loaded, if not, use premium backup fallback
                    const testImg = new Image();
                    const path = backgrounds[currentBgIndex].replace("url('", "").replace("')", "");
                    testImg.src = path;
                    testImg.onerror = function() {
                        if (currentBgIndex < 3) {
                            hero.style.backgroundImage = fallbacks[currentBgIndex];
                        }
                    };
                }

                // Cycle background index
                currentBgIndex = (currentBgIndex + 1) % backgrounds.length;
            }
        }

        // Auto shuffle home background every 15 seconds
        setInterval(shuffleBackground, 15000);

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

        // Standard JS Navigation Router for multi-page simulation
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

        // Skills category filtering system
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

        // Dark/Light Mode toggle handler
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
            
            // Traditional bubble sorting pass comparison
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
            navigateTo('page-home'); // Ensures Home section displays immediately
            shuffleBackground();
        };
    </script>
</body>
</html>