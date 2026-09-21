import { useState } from 'react'
import { loginUser } from '../services/api'

function Login({ onRegister, onSuccess }) {
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')

    const [error, setError] = useState('')
    const [loading, setLoading] = useState(false)

    const handleLogin = async (e) => {
        e.preventDefault()

        setError('')
        setLoading(true)

        try {
            const data = await loginUser(username, password)

            localStorage.setItem(
                'access_token',
                data.access_token
            )

            localStorage.setItem(
                'username',
                data.user
            )

            onSuccess?.()

        } catch (err) {
            setError(err.message)
        } finally {
            setLoading(false)
        }
    }

    return (
        <div className="min-h-screen bg-slate-950 px-6 py-20 text-white">

            <div className="mx-auto flex min-h-[80vh] max-w-md items-center justify-center">

                <div className="w-full rounded-3xl border border-white/10 bg-white/[0.03] p-8 shadow-2xl backdrop-blur-xl">

                    <div className="mb-8">

                        <div className="mb-5 flex h-11 w-11 items-center justify-center rounded-xl bg-white font-bold text-slate-950">
                            AI
                        </div>

                        <h1 className="text-3xl font-bold tracking-tight">
                            Welcome back
                        </h1>

                        <p className="mt-2 text-sm text-slate-400">
                            Sign in to your AI engineering workspace.
                        </p>

                    </div>

                    {error && (
                        <div className="mb-5 rounded-xl border border-red-500/20 bg-red-500/10 px-4 py-3 text-sm text-red-400">
                            {error}
                        </div>
                    )}

                    <form
                        onSubmit={handleLogin}
                        className="space-y-5"
                    >

                        <div>

                            <label className="mb-2 block text-sm font-medium text-slate-300">
                                Username
                            </label>

                            <input
                                type="text"
                                value={username}
                                onChange={(e) =>
                                    setUsername(e.target.value)
                                }
                                placeholder="Enter your username"
                                required
                                className="w-full rounded-xl border border-white/10 bg-slate-900 px-4 py-3 text-sm outline-none transition placeholder:text-slate-600 focus:border-white/30"
                            />

                        </div>

                        <div>

                            <label className="mb-2 block text-sm font-medium text-slate-300">
                                Password
                            </label>

                            <input
                                type="password"
                                value={password}
                                onChange={(e) =>
                                    setPassword(e.target.value)
                                }
                                placeholder="Enter your password"
                                required
                                className="w-full rounded-xl border border-white/10 bg-slate-900 px-4 py-3 text-sm outline-none transition placeholder:text-slate-600 focus:border-white/30"
                            />

                        </div>

                        <button
                            type="submit"
                            disabled={loading}
                            className="w-full rounded-xl bg-white py-3 text-sm font-semibold text-slate-950 transition hover:bg-slate-200 disabled:cursor-not-allowed disabled:opacity-50"
                        >
                            {loading ? 'Signing in...' : 'Sign In'}
                        </button>

                    </form>

                    <p className="mt-6 text-center text-sm text-slate-500">
                        Don't have an account?{' '}

                        <button
                            type="button"
                            onClick={onRegister}
                            className="text-white hover:underline"
                        >
                            Create one
                        </button>

                    </p>

                </div>
            </div>
        </div>
    )
}

export default Login