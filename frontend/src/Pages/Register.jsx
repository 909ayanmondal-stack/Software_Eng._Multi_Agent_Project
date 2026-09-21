import { useState } from 'react'
import { registerUser } from '../services/api'

function Register({ onLogin, onSuccess }) {
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')

    const [error, setError] = useState('')
    const [success, setSuccess] = useState('')
    const [loading, setLoading] = useState(false)

    const handleRegister = async (e) => {
        e.preventDefault()

        setError('')
        setSuccess('')
        setLoading(true)

        try {
            await registerUser(username, password)

            setSuccess(
                'Account created successfully. You can now sign in.'
            )

            setUsername('')
            setPassword('')

            setTimeout(() => {
                onSuccess?.()
            }, 1000)

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
                            Create account
                        </h1>

                        <p className="mt-2 text-sm text-slate-400">
                            Start building with your AI engineering workspace.
                        </p>

                    </div>

                    {error && (
                        <div className="mb-5 rounded-xl border border-red-500/20 bg-red-500/10 px-4 py-3 text-sm text-red-400">
                            {error}
                        </div>
                    )}

                    {success && (
                        <div className="mb-5 rounded-xl border border-emerald-500/20 bg-emerald-500/10 px-4 py-3 text-sm text-emerald-400">
                            {success}
                        </div>
                    )}

                    <form
                        onSubmit={handleRegister}
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
                                placeholder="Choose a username"
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
                                placeholder="Create a password"
                                required
                                className="w-full rounded-xl border border-white/10 bg-slate-900 px-4 py-3 text-sm outline-none transition placeholder:text-slate-600"
                            />

                        </div>

                        <button
                            type="submit"
                            disabled={loading}
                            className="w-full rounded-xl bg-white py-3 text-sm font-semibold text-slate-950 transition hover:bg-slate-200 disabled:cursor-not-allowed disabled:opacity-50"
                        >
                            {loading
                                ? 'Creating account...'
                                : 'Create Account'}
                        </button>

                    </form>

                    <p className="mt-6 text-center text-sm text-slate-500">
                        Already have an account?{' '}

                        <button
                            type="button"
                            onClick={onLogin}
                            className="text-white hover:underline"
                        >
                            Sign in
                        </button>

                    </p>

                </div>
            </div>
        </div>
    )
}

export default Register