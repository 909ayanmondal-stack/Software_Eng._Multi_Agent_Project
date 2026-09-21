const agents = [
    [
        '01',
        'Requirement Analyst',
        'Understands and breaks down requirements.',
    ],
    [
        '02',
        'Architecture Agent',
        'Designs the software architecture and flow.',
    ],
    [
        '03',
        'Code Agent',
        'Generates implementation-ready code.',
    ],
    [
        '04',
        'Review Agent',
        'Reviews code and identifies improvements.',
    ],
    [
        '05',
        'Testing Agent',
        'Tests functionality and finds issues.',
    ],
]

function Workflow() {
    return (
        <section
            id="workflow"
            className="border-t border-white/10 px-6 py-24"
        >
            <div className="mx-auto max-w-7xl">

                <p className="text-sm uppercase tracking-widest text-slate-500">
                    Multi-Agent Workflow
                </p>

                <h2 className="mt-4 text-4xl font-bold tracking-tight">
                    One workflow.

                    <span className="text-slate-500">
                        {' '}Multiple specialized agents.
                    </span>
                </h2>

                <div className="mt-14 grid gap-4 md:grid-cols-2 lg:grid-cols-5">

                    {agents.map(([number, title, description]) => (
                        <div
                            key={number}
                            className="rounded-2xl border border-white/10 bg-white/[0.03] p-6 transition hover:-translate-y-1 hover:border-white/20 hover:bg-white/[0.06]"
                        >

                            <span className="text-sm text-slate-600">
                                {number}
                            </span>

                            <h3 className="mt-8 text-lg font-semibold">
                                {title}
                            </h3>

                            <p className="mt-3 text-sm leading-6 text-slate-400">
                                {description}
                            </p>

                        </div>
                    ))}

                </div>
            </div>
        </section>
    )
}

export default Workflow