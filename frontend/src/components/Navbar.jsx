function Navbar({ onLogin, onRegister }) {
    return (
        <nav className="fixed top-0 z-50 w-full border-b border-white/10 bg-slate-950/80 backdrop-blur-xl">
            <div className="mx-auto flex h-16 max-w-7xl items-center justify-between px-6">

                <div className="flex items-center gap-3">
                    <div className="flex h-9 w-9 items-center justify-center rounded-xl bg-white text-sm font-bold text-slate-950">
                        AI
                    </div>

                    <span className="text-lg font-semibold tracking-tight">
                        Software Engineering AI
                    </span>
                </div>

                <div className="hidden items-center gap-8 text-sm text-slate-400 md:flex">
                    <a
                        href="#workflow"
                        className="transition hover:text-white"
                    >
                        Workflow
                    </a>

                    <a
                        href="#features"
                        className="transition hover:text-white"
                    >
                        Features
                    </a>
                </div>

                <div className="flex items-center gap-3">

                    <button
                        onClick={onLogin}
                        className="hidden rounded-lg px-4 py-2 text-sm font-medium text-slate-300 transition hover:text-white sm:block"
                    >
                        Sign In
                    </button>

                    <button
                        onClick={onRegister}
                        className="rounded-lg bg-white px-4 py-2 text-sm font-semibold text-slate-950 transition hover:bg-slate-200"
                    >
                        Get Started
                    </button>

                </div>
            </div>
        </nav>
    )
}

export default Navbar