function Hero({ onLogin, onRegister }) {
    return (
        <section className="relative flex min-h-screen items-center justify-center overflow-hidden px-6 pt-16">

            <div className="absolute inset-0 -z-10 bg-[radial-gradient(circle_at_top,#1e293b_0%,#020617_45%)]" />

            <div className="mx-auto max-w-5xl text-center">

                <div className="mb-6 inline-flex rounded-full border border-white/10 bg-white/5 px-4 py-2 text-sm text-slate-300 backdrop-blur">
                    AI-Powered Software Engineering
                </div>

                <h1 className="text-5xl font-bold tracking-tight text-white sm:text-6xl lg:text-7xl">
                    Build software with

                    <span className="block text-slate-400">
                        intelligent AI agents.
                    </span>
                </h1>

                <p className="mx-auto mt-6 max-w-2xl text-lg leading-8 text-slate-400">
                    Analyze requirements, design architecture, generate code, review,
                    test, and improve software through a collaborative multi-agent
                    workflow.
                </p>

                <div className="mt-10 flex flex-col justify-center gap-4 sm:flex-row">

                    <button
                        onClick={onRegister}
                        className="rounded-xl bg-white px-6 py-3 font-semibold text-slate-950 transition hover:bg-slate-200"
                    >
                        Start Building
                    </button>

                    <button
                        onClick={onLogin}
                        className="rounded-xl border border-white/10 bg-white/5 px-6 py-3 font-semibold text-white backdrop-blur transition hover:bg-white/10"
                    >
                        Sign In
                    </button>

                </div>
            </div>
        </section>
    )
}

export default Hero