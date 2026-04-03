function ClientList({ clients }){
    return (
        <div>
            {clients.map(client => (
                <div key={client.id} className="bg-white rounded-lg shadow p-4 mb-3">
                    <p className="font-semibold text-gray-800">{client.first_name} {client.last_name}</p>
                    <p className="text-gray-500 text-sm">{client.phone_number}</p>
                </div>
            ))}
        </div>
    )
}

export default ClientList
