const API_URL =
    import.meta.env.VITE_API_URL ||
    'http://127.0.0.1:8000'

export async function loginUser(username, password) {
    const response = await fetch(
        `${API_URL}/auth/login`,
        {
            method: 'POST',

            headers: {
                'Content-Type': 'application/json',
            },

            body: JSON.stringify({
                username,
                password,
            }),
        }
    )

    const data = await response.json()

    if (!response.ok) {
        throw new Error(
            data.detail ||
            data.message ||
            'Login failed'
        )
    }

    return data
}

export async function registerUser(
    username,
    password
) {
    const response = await fetch(
        `${API_URL}/auth/register`,
        {
            method: 'POST',

            headers: {
                'Content-Type': 'application/json',
            },

            body: JSON.stringify({
                username,
                password,
            }),
        }
    )

    const data = await response.json()

    if (!response.ok) {
        throw new Error(
            data.detail ||
            data.message ||
            'Registration failed'
        )
    }

    return data
}

export async function getProfile() {
    const token =
        localStorage.getItem('access_token')

    const response = await fetch(
        `${API_URL}/auth/profile`,
        {
            headers: {
                Authorization: `Bearer ${token}`,
            },
        }
    )

    const data = await response.json()

    if (!response.ok) {
        throw new Error(
            data.detail ||
            'Failed to load profile'
        )
    }

    return data
}

export async function logoutUser() {
    const token =
        localStorage.getItem('access_token')

    try {
        await fetch(
            `${API_URL}/auth/logout`,
            {
                method: 'POST',

                headers: {
                    Authorization: `Bearer ${token}`,
                },
            }
        )
    } finally {
        localStorage.removeItem(
            'access_token'
        )

        localStorage.removeItem(
            'username'
        )
    }
}