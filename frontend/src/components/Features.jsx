const features = [
    {
        title: 'Requirement Analysis',
        description:
            'Turn natural-language requirements into structured specifications.',
    },
    {
        title: 'Intelligent Planning',
        description:
            'Create clear development plans and technical architecture.',
    },
    {
        title: 'Code Generation',
        description:
            'Generate implementation-ready code with specialized agents.',
    },
    {
        title: 'Automated Review',
        description:
            'Analyze generated code for quality, errors, and improvements.',
    },
    {
        title: 'Testing',
        description:
            'Validate functionality and identify potential issues.',
    },
    {
        title: 'Continuous Improvement',
        description:
            'Iteratively improve the solution through agent feedback.',
    },
]

function Features() {
    return (
        <section
            id="features"
            className="border-t border-white/10 px-6 py-24"
        >
            <div className="mx-auto max-w-7xl">

                <div className="max-w-2xl">

                    <p className="text-sm font-medium uppercase tracking-widest text-slate-500">
                        Capabilities
                    </p>

                    <h2 className="mt-4 text-4xl font-bold tracking-tight">
                        Everything your software workflow needs.
                    </h2>

                </div>

                <div className="mt-14 grid gap-4 md:grid-cols-2 lg:grid-cols-3">

                    {features.map((feature) => (
                        <div
                            key={feature.title}
                            className="group rounded-2xl border border-white/10 bg-white/[0.03] p-7 transition duration-300 hover:-translate-y-1 hover:border-white/20 hover:bg-white/[0.06]"
                        >

                            <div className="mb-8 flex h-10 w-10 items-center justify-center rounded-xl border border-white/10 bg-white/5 text-sm">
                                AI
                            </div>

                            <h3 className="text-lg font-semibold">
                                {feature.title}
                            </h3>

                            <p className="mt-3 text-sm leading-6 text-slate-400">
                                {feature.description}
                            </p>

                        </div>
                    ))}

                </div>
            </div>
        </section>
    )
}

export default Features