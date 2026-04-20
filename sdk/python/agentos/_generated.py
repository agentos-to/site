"""Auto-generated TypedDict classes from shape YAML — do not edit.

Generated from 73 shapes.
Regenerate with: python generate.py --lang python
"""

from __future__ import annotations

from typing import Any, TypedDict

class Account(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    accountType: str
    bio: str
    color: str
    displayName: str
    email: str
    handle: str
    identifier: str
    isActive: bool
    joinedDate: str
    lastActive: str
    phone: str
    at: Actor
    authenticatedVia: Account
    followers: list[Account]
    follows: list[Account]
    operator: Actor
    owner: Person
    previousIdentity: list[Account]
    protocol: Protocol
    via: Product


class Activity(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    action: str
    changedKeys: list[str]
    duration: float
    published: str
    success: bool
    toolName: str
    folder: Folder
    session: McpSession


class Actor(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    actorType: str


class Agent(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    actorType: str
    model: str
    provider: str
    sessionId: str


class Aircraft(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    aisle: str
    availability: str
    barcode: str
    calories: float
    categories: list[str]
    category: str
    currency: str
    department: str
    iataCode: str
    icaoCode: str
    images: Any
    model: str
    novaGroup: int
    nutritionScore: str
    originalPrice: str
    originalPriceAmount: float
    price: str
    priceAmount: float
    quantity: int
    rangeKm: int
    seatCapacity: int
    servingSize: str
    sku: str
    soldByWeight: bool
    variant: str
    weight: str
    weightUnit: str
    weightValue: float
    brand: Brand
    manufacturer: Organization
    tagged: list[Tag]


class Album(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    contains: list[Image]


class App(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    app_id: str
    description: str
    entity_types: Any
    standalone: bool


class Book(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    aisle: str
    availability: str
    awardsWon: list[str]
    barcode: str
    calories: float
    categories: list[str]
    category: str
    characters: list[str]
    currency: str
    department: str
    format: str
    genres: list[str]
    images: Any
    isbn: str
    isbn13: str
    language: str
    novaGroup: int
    nutritionScore: str
    originalPrice: str
    originalPriceAmount: float
    originalTitle: str
    pages: int
    places: list[str]
    price: str
    priceAmount: float
    quantity: int
    series: str
    servingSize: str
    sku: str
    soldByWeight: bool
    weight: str
    weightUnit: str
    weightValue: float
    brand: Brand
    contributors: list[Person]
    manufacturer: Organization
    publisher: Organization
    tagged: list[Tag]
    writtenBy: Person


class Branch(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    ahead: int
    behind: int
    commit: str
    isCurrent: bool
    isRemote: bool
    upstream: str
    repository: Repository


class Brand(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    country: str
    founded: str
    tagline: str
    ownedBy: Organization
    website: Website


class Calendar(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    accessRole: str
    backgroundColor: str
    calendarId: str
    color: str
    foregroundColor: str
    isPrimary: bool
    isReadonly: bool
    source: str
    timezone: str
    events: list[Event]
    owner: Person


class Channel(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    banner: str
    at: Actor


class Class(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    activityType: str
    allDay: bool
    capacity: int
    dateUpdated: str
    endDate: str
    eventType: str
    icalUid: str
    isFull: bool
    recurrence: list[str]
    showAs: str
    sourceTitle: str
    sourceUrl: str
    spotsRemaining: int
    startDate: str
    status: str
    timezone: str
    visibility: str
    at: Actor
    attachments: list[File]
    creator: Person
    instructor: Person
    involves: list[Person]
    location: Place
    organizer: Person
    venue: Place


class Community(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    privacy: str
    at: Actor


class Conversation(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    accountEmail: str
    cwd: str
    gitBranch: str
    isArchived: bool
    isGroup: bool
    messageCount: int
    unreadCount: int
    at: Actor
    in_: Folder  # in
    message: list[Message]
    participant: list[Actor]


class DnsRecord(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    domain: str
    recordName: str
    recordType: str
    ttl: int
    values: list[str]


class Document(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    abstract: str
    contentType: str
    encoding: str
    filename: str
    format: str
    kind: str
    language: str
    lineCount: int
    mimeType: str
    path: str
    sha: str
    size: int
    tableOfContents: str
    wordCount: int
    attachedTo: Message
    author: Actor
    citedBy: list[Document]
    references: list[Document]
    repository: Repository


class Domain(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    autoRenew: bool
    expiresAt: str
    nameservers: list[str]
    registrar: str
    status: str


class Email(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    accountEmail: str
    attachments: Any
    authResults: str
    bccRaw: str
    bodyHtml: str
    ccRaw: str
    deliveredTo: str
    hasAttachments: bool
    inReplyTo: str
    isAutomated: bool
    isDraft: bool
    isOutgoing: bool
    isSent: bool
    isSpam: bool
    isStarred: bool
    isTrash: bool
    isUnread: bool
    listId: str
    mailer: str
    manageSubscription: str
    messageId: str
    precedence: str
    references: str
    replyTo: str
    returnPath: str
    sizeEstimate: int
    subject: str
    toRaw: str
    unsubscribe: str
    unsubscribeOneClick: bool
    at: Actor
    bcc: list[Account]
    cc: list[Account]
    ccDomain: list[Domain]
    domain: Domain
    from_: Account  # from
    inConversation: Conversation
    repliesTo: Message
    tag: list[Tag]
    to: list[Account]
    toDomain: list[Domain]
    toolCalls: list[ToolCall]


class Episode(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    durationMs: int
    episodeNumber: int
    seasonNumber: int
    guest: list[Person]
    series: Podcast
    transcribe: Transcript


class Event(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    allDay: bool
    dateUpdated: str
    endDate: str
    eventType: str
    icalUid: str
    recurrence: list[str]
    showAs: str
    sourceTitle: str
    sourceUrl: str
    startDate: str
    status: str
    timezone: str
    visibility: str
    at: Actor
    attachments: list[File]
    creator: Person
    involves: list[Person]
    location: Place
    organizer: Person


class File(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    encoding: str
    filename: str
    format: str
    kind: str
    lineCount: int
    mimeType: str
    path: str
    sha: str
    size: int
    attachedTo: Message
    repository: Repository


class Folder(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    hasReadme: bool
    path: str
    workspaceType: str
    contains: list[File]
    repository: Repository


class GitCommit(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    additions: int
    committedAt: str
    deletions: int
    filesChanged: int
    message: str
    sha: str
    shortHash: str
    author: Account
    committer: Account
    parent: GitCommit
    repository: Repository


class Group(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    category: str
    memberCount: int


class Hardware(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    aisle: str
    availability: str
    barcode: str
    calories: float
    categories: list[str]
    category: str
    currency: str
    department: str
    images: Any
    modelNumber: str
    novaGroup: int
    nutritionScore: str
    originalPrice: str
    originalPriceAmount: float
    price: str
    priceAmount: float
    quantity: int
    serialNumber: str
    servingSize: str
    sku: str
    soldByWeight: bool
    specs: Any
    weight: str
    weightUnit: str
    weightValue: float
    brand: Brand
    manufacturer: Organization
    tagged: list[Tag]


class Image(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    altText: str
    appName: str
    displayId: int
    displayIndex: int
    encoding: str
    filename: str
    format: str
    height: int
    kind: str
    lineCount: int
    mimeType: str
    path: str
    sha: str
    size: int
    width: int
    windowId: int
    attachedTo: Message
    repository: Repository


class Invitation(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    acceptedAt: str
    email: str
    expiresAt: str
    invitationType: str
    message: str
    revokedAt: str
    role: str
    status: str
    token: str
    at: Actor
    invitee: Account
    inviter: Account
    organization: Organization


class Job(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    boot_epoch: int
    config: Any
    kind: str
    status: str
    produced: Conversation
    requested_by: Account


class Leg(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    arrivalTime: str
    cabinClass: str
    carbonEmissions: Any
    departureTime: str
    duration: str
    durationMinutes: int
    flightNumber: str
    layoverMinutes: int
    polyline: str
    sequence: int
    trace: Any
    tracePointCount: int
    vehicleType: str
    aircraft: Aircraft
    carrier: Organization
    destination: Place
    origin: Place
    trip: Trip


class List(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    isDefault: bool
    isPublic: bool
    listId: str
    listType: str
    privacy: str
    at: Actor
    belongsTo: Account
    contains: list[Product]


class LoadedModel(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    digest: str
    expiresAt: str
    quantization: str
    size: str
    sizeVram: int
    vramUsage: str


class McpSession(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    client: str
    endedAt: str
    gitBranch: str
    messageCount: int
    projectId: str
    sessionType: str
    startedAt: str
    tokenCount: int
    folder: Folder
    participant: Actor


class Meeting(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    allDay: bool
    calendarLink: str
    conferenceProvider: str
    dateUpdated: str
    endDate: str
    eventType: str
    icalUid: str
    isVirtual: bool
    meetingUrl: str
    phoneDialIn: str
    recurrence: list[str]
    showAs: str
    sourceTitle: str
    sourceUrl: str
    startDate: str
    status: str
    timezone: str
    visibility: str
    at: Actor
    attachments: list[File]
    creator: Person
    involves: list[Person]
    location: Place
    organizer: Person
    transcribe: Transcript


class Memex(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    description: str
    edgeCount: int
    filePath: str
    fileSize: str
    nodeCount: int
    origin: str
    published: bool
    snapshotOf: str
    forkedFrom: Memex
    owner: Person
    snapshots: list[Memex]


class Message(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    isOutgoing: bool
    isStarred: bool
    at: Actor
    from_: Actor  # from
    inConversation: Conversation
    repliesTo: Message
    toolCalls: list[ToolCall]


class Model(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    contextLength: int
    contextWindow: int
    digest: str
    family: str
    format: str
    maxOutput: int
    modality: list[str]
    modelType: str
    parameterSize: str
    pricingInput: str
    pricingOutput: str
    quantization: str
    quantizationLevel: str
    size: str
    at: Actor


class Note(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    isPinned: bool
    noteType: str
    createdBy: Person
    extractedFrom: Webpage
    references: list[Note]


class Offer(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    availability: str
    bookingToken: str
    currency: str
    offerType: str
    price: float
    validFrom: str
    validUntil: str
    for_: Product  # for
    offeredBy: Organization
    trips: list[Trip]


class Order(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    currency: str
    deliveryDate: str
    deliveryFee: float
    eta: str
    fareBreakdown: Any
    orderDate: str
    orderId: str
    originalTotal: str
    originalTotalAmount: float
    savings: float
    status: str
    subtotal: float
    summary: str
    taxes: float
    tipAmount: float
    total: str
    totalAmount: float
    at: Actor
    contains: list[Product]
    delivery: Trip
    shippingAddress: Place
    store: Place
    tracking: Webpage


class Organization(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    actorType: str
    founded: str
    industry: str
    domain: Domain
    headquarters: Place
    member: list[Person]
    website: Website


class Person(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    about: str
    actorType: str
    birthday: str
    firstName: str
    gender: str
    joinedDate: str
    lastActive: str
    lastName: str
    middleName: str
    nickname: str
    notes: str
    accounts: list[Account]
    location: Place
    roles: list[Role]
    website: Website


class Place(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    accuracy: str
    businessStatus: str
    categories: list[str]
    city: str
    country: str
    countryCode: str
    district: str
    featureType: str
    fullAddress: str
    googlePlaceId: str
    hours: Any
    latitude: float
    locality: str
    longitude: float
    mapboxId: str
    neighborhood: str
    phone: str
    placeFormatted: str
    postalCode: str
    priceLevel: str
    rating: float
    region: str
    reviewCount: int
    street: str
    streetNumber: str
    timezone: str
    website: str
    wikidataId: str
    brand: Organization
    offers: list[Product]


class Playlist(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    isDefault: bool
    isPublic: bool
    listId: str
    listType: str
    privacy: str
    at: Actor
    belongsTo: Account
    contains: list[Video]


class Podcast(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    feedUrl: str
    at: Actor
    episode: list[Episode]
    host: list[Person]


class Post(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    externalUrl: str
    postType: str
    attachment: list[File]
    contains: list[Video]
    media: list[Image]
    postedBy: Account
    publish: Community
    replies: list[Post]
    repliesTo: Post


class Product(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    aisle: str
    availability: str
    barcode: str
    calories: float
    categories: list[str]
    category: str
    currency: str
    department: str
    images: Any
    novaGroup: int
    nutritionScore: str
    originalPrice: str
    originalPriceAmount: float
    price: str
    priceAmount: float
    quantity: int
    servingSize: str
    sku: str
    soldByWeight: bool
    weight: str
    weightUnit: str
    weightValue: float
    brand: Brand
    manufacturer: Organization
    tagged: list[Tag]


class Project(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    color: str
    state: str


class Protocol(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    homepage: str
    rfc: str
    wikidataId: str


class Quote(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    context: str
    year: int


class Repository(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    defaultBranch: str
    forks: int
    isArchived: bool
    isPrivate: bool
    language: str
    license: str
    openIssues: int
    size: int
    stars: int
    topics: list[str]
    forkedFrom: Repository
    owner: Account


class Result(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    indexedAt: str
    resultType: str


class Review(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    externalUrl: str
    isVerified: bool
    postType: str
    rating: float
    ratingMax: float
    tags: list[str]
    attachment: list[File]
    contains: list[Video]
    media: list[Image]
    postedBy: Account
    publish: Community
    replies: list[Post]
    repliesTo: Post
    reviews: Product


class Role(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    department: str
    endDate: str
    roleType: str
    startDate: str
    title: str
    organization: Organization
    person: Person


class Search(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    query: str
    resultCount: int
    searchCount: int
    searchedAt: str


class Shelf(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    isDefault: bool
    isExclusive: bool
    isPublic: bool
    listId: str
    listType: str
    privacy: str
    at: Actor
    belongsTo: Account
    contains: list[Book]


class Shortcut(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    builtin: bool
    filter: str
    target: str
    skill: Skill


class Simulation(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    actionCount: int
    endedAt: str
    graphMode: str
    profile: str
    startedAt: str
    status: str
    task: str
    writeCount: int
    agent: Agent
    forkedFrom: Simulation
    mountedMemex: list[Memex]
    primaryMemex: Memex
    startedBy: Person
    tether: Hardware


class Skill(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    color: str
    description: str
    error: str
    skillId: str
    status: str
    privacyPolicy: Webpage
    termsOfService: Webpage
    website: Website


class Software(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    aisle: str
    availability: str
    barcode: str
    calories: float
    categories: list[str]
    category: str
    currency: str
    department: str
    images: Any
    license: str
    novaGroup: int
    nutritionScore: str
    openSource: bool
    originalPrice: str
    originalPriceAmount: float
    platform: list[str]
    price: str
    priceAmount: float
    quantity: int
    repositoryUrl: str
    servingSize: str
    sku: str
    soldByWeight: bool
    version: str
    weight: str
    weightUnit: str
    weightValue: float
    brand: Brand
    developer: Organization
    manufacturer: Organization
    repository: Repository
    tagged: list[Tag]


class Source(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    address: str
    description: str
    enabled: bool
    lastSynced: str
    scanner: str
    sourceId: str
    folder: Folder


class Spec(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    encoding: str
    filename: str
    format: str
    kind: str
    labels: list[str]
    lineCount: int
    mimeType: str
    path: str
    priority: int
    problem: str
    remoteId: str
    sha: str
    size: int
    startedAt: str
    state: str
    successCriteria: str
    targetDate: str
    assignedTo: Person
    attachedTo: Message
    blockedBy: list[Task]
    blocks: list[Task]
    children: list[Task]
    dependsOn: list[Spec]
    parent: Task
    project: Project
    repository: Repository
    supersedes: list[Spec]


class Tag(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    color: str
    tagType: str


class Task(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    labels: list[str]
    priority: int
    remoteId: str
    startedAt: str
    state: str
    targetDate: str
    assignedTo: Person
    blockedBy: list[Task]
    blocks: list[Task]
    children: list[Task]
    parent: Task
    project: Project
    repository: Repository


class Theme(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    colorScheme: str
    description: str
    family: str
    themeId: str
    wallpaper: Image


class ToolCall(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    durationMs: int
    input: str
    isError: bool
    output: str
    from_: Actor  # from
    inMessage: Message
    platform: Product
    repliesTo: ToolCall


class Transaction(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    amount: float
    balance: float
    category: str
    currency: str
    details: Any
    notes: str
    pending: bool
    postingDate: str
    recurring: bool
    type: str
    account: Account


class Transcript(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    contentRole: str
    durationMs: int
    language: str
    segmentCount: int
    segments: Any
    sourceType: str


class Trip(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    arrivalTime: str
    bookingToken: str
    cabinClass: str
    carbonEmissions: Any
    currency: str
    departureTime: str
    distance: str
    duration: str
    durationMinutes: int
    fare: str
    fareAmount: float
    isScheduled: bool
    isSurge: bool
    rating: str
    status: str
    stops: int
    trackingUrl: str
    tripType: str
    vehicleType: str
    carrier: Organization
    destination: Place
    driver: Person
    legs: list[Leg]
    order: Order
    origin: Place


class Video(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    codec: str
    durationMs: int
    encoding: str
    filename: str
    format: str
    frameRate: float
    kind: str
    lineCount: int
    mimeType: str
    path: str
    resolution: str
    sha: str
    size: int
    addTo: Playlist
    attachedTo: Message
    channel: Channel
    repository: Repository
    transcribe: Transcript


class Volume(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    filesystem: str
    freeBytes: int
    path: str
    readOnly: bool
    removable: bool
    totalBytes: int
    usedBytes: int
    volumeType: str
    contains: list[Folder]


class Webpage(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    contentType: str
    error: str
    lastVisitUnix: int
    visitCount: int


class Website(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    anonymous: bool
    claimToken: str
    claimUrl: str
    expiresAt: str
    status: str
    versionId: str
    domain: Domain
    ownedBy: Organization


# Raw YAML bodies — consumed by the skill worker to attach
# `__shape_yaml__` on every @returns(shape) response.
SHAPE_YAMLS: dict[str, str] = {
    'account': 'plural: accounts\nidentity:\n- at\n- identifier\nsubtitle: identifier\nfields:\n  identifier: string\n  handle: string\n  displayName: string\n  email: string\n  phone: string\n  bio: text\n  accountType: string\n  color: string\n  isActive: boolean\n  joinedDate: datetime\n  lastActive: datetime\nrelations:\n  at: actor\n  via: product\n  operator: actor\n  protocol: protocol\n  owner: person\n  authenticatedVia: account\n  previousIdentity: account[]\n  follows: account[]\n  followers: account[]\nprior_art:\n- source: ActivityPub Actor model\n  url: https://www.w3.org/TR/activitypub/\n  notes: Account id is a URL; Server/Application/Operator are separate Actor objects.\n    We adopt the same separation but ground each in graph nodes rather than URLs,\n    so node lifecycle (rebrand, merge) propagates to all referencing accounts.\n- source: schema.org Offer.seller union\n  url: https://schema.org/Offer\n  notes: "seller: Person | Organization. The `actor` shape (which `at` and `operator`\\\n    \\ target) is our existing union of person/org/agent \\u2014 same pattern."\n- source: OpenID Connect Core 1.0 (`iss`/`sub`)\n  url: https://openid.net/specs/openid-connect-core-1_0.html\n  notes: OIDC keeps issuer as opaque URL because there\'s no shared graph across token\n    issuers. We have a graph; we replace the URL with a graph node, gaining mutability\n    and traversal at the cost of requiring a node to exist before an account can reference\n    it. Trade is worth it.\n- source: WebFinger (RFC 7033)\n  url: https://datatracker.ietf.org/doc/html/rfc7033\n  notes: \'Resolves issuer+identifier pairs to profile metadata. Our identifier aligns\n    with WebFinger\'\'s acct: URI scheme (user@host), but the `host` part becomes a\n    graph node (not a string).\'\n- source: vCard 4.0 (RFC 6350)\n  url: https://datatracker.ietf.org/doc/html/rfc6350\n  notes: Defines displayName/email/phone/org in contact cards. We adopt vCard\'s contact\n    semantics for the human-readable fields.\n',
    'activity': 'plural: activities\nsubtitle: action\nicon: activity\nfields:\n  action: string\n  published: datetime\n  changedKeys: string[]\n  toolName: string\n  duration: number\n  success: boolean\nrelations:\n  session: mcp_session\n  folder: folder\nprior_art:\n- source: ActivityStreams 2.0\n  url: https://www.w3.org/TR/activitystreams-core/\n  notes: AS2\'s Create/Update/Delete activities match our action values. We diverge\n    by tracking changedKeys explicitly instead of encoding full object replacement.\n- source: OpenTelemetry Traces\n  url: https://opentelemetry.io/docs/concepts/signals/traces/\n  notes: "Closest fit for toolName/duration/success \\u2014 span-shaped. Our activity\\\n    \\ is closer to a span event than a full span."\n',
    'actor': 'plural: actors\nsubtitle: actorType\nfields:\n  actorType: string\nprior_art:\n- source: FOAF Agent\n  url: http://xmlns.com/foaf/spec/#term_Agent\n  notes: FOAF Agent is the base class for Person, Organization, and Group. Our actorType\n    mirrors FOAF\'s agent taxonomy.\n- source: ActivityStreams 2.0 Actor\n  url: https://www.w3.org/TR/activitystreams-vocabulary/#actor-types\n  notes: "AS2 defines Actor types (Person, Organization, Group, Service, Application).\\\n    \\ Our agent \\u2248 Service/Application."\n',
    'agent': "plural: agents\nsubtitle: model\nalso:\n- actor\nfields:\n  model: string\n  provider: string\n  sessionId: string\nprior_art:\n- source: ActivityStreams 2.0 Service\n  url: https://www.w3.org/TR/activitystreams-vocabulary/#dfn-service\n  notes: AS2's Service Actor is the closest peer for an automated agent. We add model/provider/sessionId\n    for AI-specific lineage.\n- source: Anthropic Tool Use API (Claude)\n  url: https://docs.anthropic.com/en/docs/build-with-claude/tool-use\n  notes: Mirrors our model/provider fields. sessionId groups related tool invocations\n    from a single agent run.\n",
    'aircraft': 'plural: aircraft\nidentity: icaoCode\nsubtitle: model\nalso:\n- product\nfields:\n  model: string\n  variant: string\n  seatCapacity: integer\n  rangeKm: integer\n  iataCode: string\n  icaoCode: string\nrelations:\n  manufacturer: organization\nprior_art:\n- source: ICAO Aircraft Type Designators (Doc 8643)\n  url: https://www.icao.int/publications/DOC8643/Pages/Search.aspx\n  notes: Our icaoCode is the canonical 4-char type code (B738, A320); iataCode is\n    the 3-char IATA equivalent (738, 320).\n- source: schema.org/Vehicle\n  url: https://schema.org/Vehicle\n  notes: Our model/seatCapacity map to vehicleModelDate/vehicleSeatingCapacity; manufacturer\n    matches directly.\n',
    'album': 'plural: albums\nidentity:\n- id\nsubtitle: id\nicon: images\nfields:\n  id: string\nrelations:\n  contains: image[]\nprior_art:\n- source: Apple Photos Album / IPTC PhotoMetadata\n  url: https://www.iptc.org/std/photometadata/specification/IPTC-PhotoMetadata\n  notes: "Albums are the simplest photo-grouping primitive. No EXIF, no date range\\\n    \\ \\u2014 just a named bucket. IPTC\'s \\"Album\\" PMV is the de-facto interchange\\\n    \\ format for this."\n',
    'app': 'plural: apps\nidentity:\n- id\nsubtitle: description\nicon: app-window\nfields:\n  id: string\n  app_id: string\n  standalone: boolean\n  description: string\n  entity_types: json\nprior_art:\n- source: Desktop Entry Specification (freedesktop.org)\n  url: https://specifications.freedesktop.org/desktop-entry-spec/latest/\n  notes: "Apps mirror .desktop entries \\u2014 a user-facing name, a description, and\\\n    \\ metadata about what categories/file-types the app handles. Our entity_types\\\n    \\ plays the role of MimeType."\n',
    'book': 'plural: books\nidentity_any:\n- isbn13\n- isbn\nsubtitle: author\nalso:\n- product\nfields:\n  isbn: string\n  isbn13: string\n  pages: integer\n  genres: string[]\n  series: string\n  format: string\n  language: string\n  originalTitle: string\n  places: string[]\n  characters: string[]\n  awardsWon: string[]\nrelations:\n  writtenBy: person\n  contributors: person[]\n  publisher: organization\nprior_art:\n- source: schema.org/Book\n  url: https://schema.org/Book\n  notes: "Our isbn maps to isbn; writtenBy = author; publisher matches; pages = numberOfPages;\\\n    \\ language = inLanguage; format \\u2248 bookFormat (Hardcover/Paperback/EBook)."\n- source: ONIX for Books 3.0\n  url: https://www.editeur.org/83/Overview/\n  notes: Publishing-industry canonical. Our isbn/isbn13/pages/format/language/series/originalTitle\n    align with ONIX Product Identifier, Extent, ProductForm, Language, Collection,\n    and OriginalLanguageTitle composites.\n- source: Open Library Books API\n  url: https://openlibrary.org/developers/api\n  notes: Practical lookup by ISBN. Our genres/characters/places/awardsWon map to subjects/subject_people/subject_places/subject_times\n    (awards less standardized).\n',
    'branch': 'plural: branches\nsubtitle: commit\nfields:\n  commit: string\n  upstream: string\n  ahead: integer\n  behind: integer\n  isCurrent: boolean\n  isRemote: boolean\nrelations:\n  repository: repository\nprior_art:\n- source: "Git Internals \\u2014 Branches"\n  url: https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell\n  notes: A branch is a movable pointer to a commit. Our commit field is the HEAD sha;\n    ahead/behind mirror `git rev-list --count`.\n- source: "GitHub REST \\u2014 branches"\n  url: https://docs.github.com/en/rest/branches/branches\n  notes: "Practical API surface. Our upstream \\u2248 the remote tracking ref; we flatten\\\n    \\ protection/commit metadata that GitHub nests."\n',
    'brand': 'plural: brands\nidentity: url\nsubtitle: tagline\nfields:\n  tagline: string\n  founded: datetime\n  country: string\nrelations:\n  ownedBy: organization\n  website: website\nprior_art:\n- source: schema.org/Brand\n  url: https://schema.org/Brand\n  notes: "Our tagline \\u2248 slogan; founded = foundingDate; ownedBy \\u2248 parentOrganization\\\n    \\ (on the owning Organization)."\n- source: Wikidata (Brand, Q431289)\n  url: https://www.wikidata.org/wiki/Q431289\n  notes: Cross-reference identity for dedupe. country maps to P17 (country); founded\n    to P571 (inception); ownedBy to P127 (owned by).\n',
    'calendar': 'plural: calendars\nidentity:\n- at\n- calendarId\nsubtitle: source\nfields:\n  calendarId: string\n  color: string\n  backgroundColor: string\n  foregroundColor: string\n  isPrimary: boolean\n  isReadonly: boolean\n  accessRole: string\n  source: string\n  timezone: string\nrelations:\n  owner: person\n  events: event[]\nprior_art:\n- source: RFC 5545 VCALENDAR\n  url: https://datatracker.ietf.org/doc/html/rfc5545\n  notes: "Our calendarId \\u2248 VCALENDAR\'s X-WR-CALID; timezone = X-WR-TIMEZONE;\\\n    \\ events relation mirrors VCALENDAR\'s VEVENT components."\n- source: CalDAV (RFC 4791)\n  url: https://datatracker.ietf.org/doc/html/rfc4791\n  notes: CalDAV calendar collections define accessRole semantics (owner/writer/reader)\n    that match our field directly.\n- source: Google Calendar API CalendarList\n  url: https://developers.google.com/calendar/api/v3/reference/calendarList\n  notes: Practical API mirror. Our color/backgroundColor/foregroundColor, isPrimary,\n    accessRole come from Google\'s CalendarList resource.\n',
    'channel': 'plural: channels\nidentity:\n- at\n- id\nfields:\n  banner: url\nrelations:\n  at: actor\nprior_art:\n- source: ActivityStreams 2.0 Collection\n  url: https://www.w3.org/TR/activitystreams-vocabulary/#dfn-collection\n  notes: A channel is a platform-specific Collection of media items. Our banner is\n    channel branding; AS2 doesn\'t model that directly.\n- source: "YouTube Data API \\u2014 Channel resource"\n  url: https://developers.google.com/youtube/v3/docs/channels\n  notes: Practical source. Our channel id/banner map to YouTube\'s channelId and brandingSettings.image.bannerExternalUrl.\n- source: RSS 2.0 <channel>\n  url: https://www.rssboard.org/rss-specification\n  notes: "Original \\"channel\\" concept \\u2014 a grouped feed with title, image, and\\\n    \\ items. Our channel is the same pattern for video."\n',
    'class': 'plural: classes\nsubtitle: activityType\nalso:\n- event\nfields:\n  activityType: string\n  capacity: integer\n  spotsRemaining: integer\n  isFull: boolean\nrelations:\n  instructor: person\n  venue: place\nprior_art:\n- source: schema.org/EducationEvent\n  url: https://schema.org/EducationEvent\n  notes: "schema.org\'s closest peer for a bookable class. Our instructor = performer;\\\n    \\ capacity = maximumAttendeeCapacity; spotsRemaining \\u2248 remainingAttendeeCapacity."\n- source: schema.org/ExerciseAction\n  url: https://schema.org/ExerciseAction\n  notes: "Fitness-specific vocabulary: activityType \\u2248 exerciseType; venue matches\\\n    \\ directly as location."\n- source: Mindbody Public API (class schedules)\n  url: https://developers.mindbodyonline.com/PublicDocumentation/V6\n  notes: Practical API mirror. Our capacity/spotsRemaining/isFull come from Mindbody\'s\n    MaxCapacity/TotalBooked/IsWaitlistAvailable.\n',
    'community': 'plural: communities\nidentity:\n- at\n- id\nsubtitle: text\nfields:\n  privacy: string\nrelations:\n  at: actor\nprior_art:\n- source: ActivityPub Group Actor\n  url: https://www.w3.org/TR/activitypub/\n  notes: "AP Group Actor models shared-inbox communities (Lemmy, Kbin, Mbin). Our\\\n    \\ privacy \\u2248 audience/to visibility."\n- source: schema.org/Organization\n  url: https://schema.org/Organization\n  notes: A community-as-organization is a loose fit; privacy has no direct schema.org\n    property.\n- source: "Reddit API \\u2014 Subreddit"\n  url: https://www.reddit.com/dev/api/#GET_subreddits_where\n  notes: "Practical source. Our privacy \\u2248 subreddit_type (public/private/ restricted);\\\n    \\ text \\u2248 public_description."\n',
    'conversation': 'plural: conversations\nidentity:\n- at\n- id\nsubtitle: text\nfields:\n  isGroup: boolean\n  isArchived: boolean\n  unreadCount: integer\n  messageCount: integer\n  accountEmail: string\n  cwd: string\n  gitBranch: string\nrelations:\n  at: actor\n  participant: actor[]\n  message: message[]\n  in: folder\nprior_art:\n- source: ActivityStreams 2.0 context/inReplyTo\n  url: https://www.w3.org/TR/activitystreams-vocabulary/#dfn-context\n  notes: "Conversations are AS2 contexts \\u2014 the thread that groups replies. Our\\\n    \\ participant[] \\u2248 to/cc/audience."\n- source: Matrix Room (m.room)\n  url: https://spec.matrix.org/latest/client-server-api/#room-events\n  notes: "Practical thread model. Our isGroup \\u2248 room.join_rules; unreadCount\\\n    \\ \\u2248 unread_notifications.highlight_count."\n- source: "Gmail API \\u2014 Thread resource"\n  url: https://developers.google.com/gmail/api/reference/rest/v1/users.threads\n  notes: "Our messageCount \\u2248 messages.length; unreadCount derived from UNREAD\\\n    \\ labels on Thread messages."\n',
    'dns_record': 'plural: dns_records\nidentity:\n- domain\n- recordType\n- recordName\nsubtitle: recordType\nfields:\n  domain: string\n  recordName: string\n  recordType: string\n  ttl: integer\n  values: string[]\nprior_art:\n- source: RFC 1035 (DNS)\n  url: https://datatracker.ietf.org/doc/html/rfc1035\n  notes: Foundational spec. Our domain/recordName/recordType/ttl/values map directly\n    to NAME/TYPE/CLASS/TTL/RDATA.\n- source: RFC 7208 (SPF), RFC 6376 (DKIM), RFC 7489 (DMARC)\n  url: https://datatracker.ietf.org/doc/html/rfc7208\n  notes: TXT-record vocabularies that frequently populate our values[] for SPF, DKIM,\n    and DMARC policy records.\n',
    'document': 'plural: documents\nsubtitle: author\nalso:\n- file\nfields:\n  contentType: string\n  language: string\n  wordCount: integer\n  abstract: text\n  tableOfContents: text\nrelations:\n  author: actor\n  references: document[]\n  citedBy: document[]\nprior_art:\n- source: Dublin Core Metadata Initiative\n  url: https://www.dublincore.org/specifications/dublin-core/dces/\n  notes: "Our contentType \\u2248 dc:format; language = dc:language; author = dc:creator;\\\n    \\ references/citedBy \\u2248 dc:relation."\n- source: schema.org/DigitalDocument\n  url: https://schema.org/DigitalDocument\n  notes: "Our abstract \\u2248 abstract; tableOfContents = hasPart or accessModeSufficient;\\\n    \\ wordCount = wordCount."\n- source: W3C Web Annotation Data Model\n  url: https://www.w3.org/TR/annotation-model/\n  notes: Our references[]/citedBy[] are annotation target/body relationships between\n    documents.\n',
    'domain': 'plural: domains\nidentity: name\nfields:\n  status: string\n  registrar: string\n  expiresAt: datetime\n  autoRenew: boolean\n  nameservers: string[]\nprior_art:\n- source: RFC 1035 (Domain Names)\n  url: https://datatracker.ietf.org/doc/html/rfc1035\n  notes: Canonical domain-name syntax + nameservers + TTL. Our nameservers are NS\n    records for the apex.\n- source: RFC 3912 (WHOIS)\n  url: https://datatracker.ietf.org/doc/html/rfc3912\n  notes: Our registrar/status/expiresAt/autoRenew come from WHOIS response fields.\n',
    'email': "plural: emails\nidentity:\n- at\n- id\nsubtitle: author\nalso:\n- message\nfields:\n  subject: string\n  messageId: string\n  inReplyTo: string\n  isUnread: boolean\n  isStarred: boolean\n  isDraft: boolean\n  isSent: boolean\n  isTrash: boolean\n  isSpam: boolean\n  hasAttachments: boolean\n  accountEmail: string\n  sizeEstimate: integer\n  references: string\n  replyTo: string\n  deliveredTo: string\n  attachments: json\n  toRaw: string\n  ccRaw: string\n  bccRaw: string\n  unsubscribe: string\n  unsubscribeOneClick: boolean\n  manageSubscription: string\n  listId: string\n  isAutomated: boolean\n  precedence: string\n  mailer: string\n  returnPath: string\n  authResults: string\n  bodyHtml: text\nrelations:\n  from: account\n  to: account[]\n  cc: account[]\n  bcc: account[]\n  domain: domain\n  toDomain: domain[]\n  ccDomain: domain[]\n  tag: tag[]\nprior_art:\n- source: RFC 5322 (Internet Message Format)\n  url: https://datatracker.ietf.org/doc/html/rfc5322\n  notes: Supersedes RFC 2822. Our messageId/inReplyTo/references/replyTo map directly\n    to Message-ID/In-Reply-To/References/Reply-To headers; toRaw/ccRaw/bccRaw are\n    the literal header values.\n- source: RFC 2369 + RFC 8058 (List headers, one-click unsubscribe)\n  url: https://datatracker.ietf.org/doc/html/rfc2369\n  notes: Our unsubscribe/unsubscribeOneClick/listId are List-Unsubscribe/List-Unsubscribe-Post/List-ID.\n    RFC 8058 defines the one-click POST semantics.\n- source: Gmail API Message resource\n  url: https://developers.google.com/gmail/api/reference/rest/v1/users.messages\n  notes: Practical API mirror. Our sizeEstimate and isUnread/isStarred/isDraft/isSent/isTrash/isSpam\n    correspond to Gmail's sizeEstimate and labelIds (UNREAD, STARRED, DRAFT, SENT,\n    TRASH, SPAM).\n",
    'episode': 'plural: episodes\nsubtitle: author\nfields:\n  durationMs: integer\n  episodeNumber: integer\n  seasonNumber: integer\nrelations:\n  series: podcast\n  transcribe: transcript\n  guest: person[]\nprior_art:\n- source: Apple Podcasts RSS Extensions (itunes:episode)\n  url: https://help.apple.com/itc/podcasts_connect/#/itcb54353390\n  notes: De-facto podcast metadata standard. Our episodeNumber/seasonNumber/ durationMs\n    = itunes:episode/itunes:season/itunes:duration.\n- source: schema.org/PodcastEpisode\n  url: https://schema.org/PodcastEpisode\n  notes: "Our series \\u2248 partOfSeries (PodcastSeries); transcribe \\u2248 transcript;\\\n    \\ guest \\u2248 actor."\n- source: Podcast Namespace (podcast:*)\n  url: https://podcastindex.org/namespace/1.0\n  notes: Modern open extension to RSS. Covers our guest, season, episode, and transcript\n    relations via podcast:person, podcast:season, etc.\n',
    'event': 'plural: events\nidentity:\n- at\n- id\nsubtitle: eventType\nfields:\n  eventType: string\n  startDate: datetime\n  endDate: datetime\n  timezone: string\n  allDay: boolean\n  recurrence: string[]\n  status: string\n  visibility: string\n  showAs: string\n  dateUpdated: datetime\n  sourceUrl: url\n  sourceTitle: string\n  icalUid: string\nrelations:\n  at: actor\n  involves: person[]\n  location: place\n  organizer: person\n  creator: person\n  attachments: file[]\nprior_art:\n- source: schema.org/Event\n  url: https://schema.org/Event\n  notes: Core event type. Our startDate/endDate map 1:1; eventType is free-form vs.\n    schema.org\'s subtype hierarchy (Concert, Conference, BusinessEvent). organizer/location\n    match directly.\n- source: RFC 5545 (iCalendar) VEVENT\n  url: https://datatracker.ietf.org/doc/html/rfc5545\n  notes: "Our icalUid is their UID; recurrence is their RRULE; status maps to STATUS\\\n    \\ (TENTATIVE/CONFIRMED/CANCELLED); showAs \\u2248 TRANSP; involves[] \\u2248 ATTENDEE."\n- source: ActivityStreams 2.0 Event\n  url: https://www.w3.org/TR/activitystreams-vocabulary/#dfn-event\n  notes: "Fediverse inbox format. Thinner than iCal \\u2014 no native recurrence or\\\n    \\ showAs; our involves[] \\u2248 attendees via as:Relationship."\n',
    'file': 'plural: files\nsubtitle: path\nfields:\n  filename: string\n  mimeType: string\n  size: integer\n  path: string\n  format: string\n  encoding: string\n  lineCount: integer\n  kind: string\n  sha: string\nrelations:\n  attachedTo: message\n  repository: repository\nprior_art:\n- source: IANA Media Types (RFC 6838)\n  url: https://datatracker.ietf.org/doc/html/rfc6838\n  notes: Our mimeType follows type/subtype syntax (text/plain, application/pdf). Canonical\n    source for format identification.\n- source: schema.org/DigitalDocument\n  url: https://schema.org/DigitalDocument\n  notes: "Our filename \\u2248 name; size \\u2248 contentSize; mimeType \\u2248 encodingFormat."\n- source: Git Internals (blob objects)\n  url: https://git-scm.com/book/en/v2/Git-Internals-Git-Objects\n  notes: Our sha is a Git blob SHA-1 (40-hex). Git\'s content-addressable model underlies\n    our repo-file identity.\n',
    'folder': 'plural: folders\nidentity: path\nsubtitle: path\nfields:\n  path: string\n  workspaceType: string\n  hasReadme: boolean\nrelations:\n  repository: repository\n  contains: file[]\nprior_art:\n- source: POSIX / Single Unix Specification\n  url: https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap03.html\n  notes: Our path is a POSIX pathname. hasReadme is AgentOS-specific (README convention\n    from repos).\n- source: schema.org/DataCatalog\n  url: https://schema.org/DataCatalog\n  notes: "Folder-as-collection loose fit. contains(file[]) \\u2248 hasPart."\n',
    'git_commit': 'plural: git_commits\nsubtitle: author\nfields:\n  sha: string\n  shortHash: string\n  message: text\n  additions: integer\n  deletions: integer\n  filesChanged: integer\n  committedAt: datetime\nrelations:\n  author: account\n  committer: account\n  repository: repository\n  parent: git_commit\nprior_art:\n- source: "Git Internals \\u2014 commit object"\n  url: https://git-scm.com/book/en/v2/Git-Internals-Git-Objects\n  notes: Our sha/shortHash/message/parent match the commit object exactly. author/committer\n    follow Git\'s distinct author-vs-committer model.\n- source: Conventional Commits 1.0\n  url: https://www.conventionalcommits.org/en/v1.0.0/\n  notes: "Practical structure for message field (type(scope): subject). Optional \\u2014\\\n    \\ we don\'t enforce but it\'s compatible."\n',
    'group': 'plural: groups\nidentity:\n- at\n- id\nsubtitle: category\nfields:\n  memberCount: integer\n  category: string\nprior_art:\n- source: schema.org/Group (via Organization/memberOf)\n  url: https://schema.org/Organization\n  notes: "schema.org models groups as Organization. Our memberCount \\u2248 numberOfEmployees\\\n    \\ loosely; category \\u2248 naics/knowsAbout."\n- source: FOAF Group\n  url: http://xmlns.com/foaf/spec/#term_Group\n  notes: Foundational social-graph vocabulary. foaf:member populates membership; category\n    has no direct FOAF peer.\n',
    'hardware': 'plural: hardware\nidentity: serialNumber\nsubtitle: author\nalso:\n- product\nfields:\n  modelNumber: string\n  serialNumber: string\n  specs: json\nrelations:\n  manufacturer: organization\nprior_art:\n- source: schema.org/Product (IndividualProduct subtype)\n  url: https://schema.org/IndividualProduct\n  notes: "Our serialNumber = serialNumber; modelNumber \\u2248 model; specs \\u2248\\\n    \\ additionalProperty (PropertyValue list)."\n- source: GS1 Global Trade Item Number (GTIN)\n  url: https://www.gs1.org/standards/id-keys/gtin\n  notes: "Hardware bar-codes are GTIN-12/13/14 \\u2014 we reuse the product shape\'s\\\n    \\ barcode alignment."\n',
    'image': 'plural: images\nalso:\n- file\nfields:\n  width: integer\n  height: integer\n  format: string\n  altText: string\n  appName: string\n  windowId: integer\n  displayId: integer\n  displayIndex: integer\nprior_art:\n- source: schema.org/ImageObject\n  url: https://schema.org/ImageObject\n  notes: "Our width/height = width/height; format \\u2248 encodingFormat; altText =\\\n    \\ caption/accessibilityCaption."\n- source: IANA Media Types (image/*)\n  url: https://www.iana.org/assignments/media-types/media-types.xhtml#image\n  notes: Our format values (PNG, JPEG, WebP, SVG) align with registered image/* media\n    types.\n- source: Exif 2.3 (JEITA CP-3451)\n  url: https://www.cipa.jp/std/documents/e/DC-008-Translation-2019-E.pdf\n  notes: Source of most image metadata fields. width/height come from Exif PixelXDimension/PixelYDimension.\n',
    'invitation': 'plural: invitations\nidentity:\n- at\n- id\nsubtitle: invitationType\nfields:\n  invitationType: string\n  email: string\n  role: string\n  status: string\n  token: string\n  expiresAt: datetime\n  acceptedAt: datetime\n  revokedAt: datetime\n  message: text\nrelations:\n  inviter: account\n  invitee: account\n  organization: organization\n  at: actor\nprior_art:\n- source: ActivityStreams 2.0 Invite activity\n  url: https://www.w3.org/TR/activitystreams-vocabulary/#dfn-invite\n  notes: AS2 Invite is the canonical fediverse verb. Our inviter = actor; invitee\n    = target; status tracks Accept/Reject/TentativeAccept responses.\n- source: iCalendar ATTENDEE + PARTSTAT (RFC 5545)\n  url: https://datatracker.ietf.org/doc/html/rfc5545\n  notes: Calendar-style invitations. Our status maps to PARTSTAT (NEEDS-ACTION/ACCEPTED/DECLINED/DELEGATED).\n- source: "SCIM 2.0 (RFC 7644) \\u2014 user provisioning"\n  url: https://datatracker.ietf.org/doc/html/rfc7644\n  notes: Enterprise invitation/provisioning. Our email/role/organization align with\n    SCIM User resource\'s email + entitlements + group membership.\n',
    'job': 'plural: jobs\nidentity:\n- name\n- boot_epoch\nsubtitle: name\nicon: play-circle\nfields:\n  name: string\n  status: string\n  kind: string\n  config: json\n  boot_epoch: integer\nrelations:\n  produced: conversation\n  requested_by: account\nprior_art:\n- source: "systemd unit \\u2014 Active/Sub state machine"\n  url: https://www.freedesktop.org/software/systemd/man/systemd.html#Concepts\n  notes: "Status mirrors systemd\'s active/sub state pairing \\u2014 our \\"running\\"\\\n    \\ \\u2248 active+running, \\"completed\\" \\u2248 inactive+dead, \\"failed\\" \\u2248\\\n    \\ failed+failed. boot_epoch plays the role of systemd\'s boot_id."\n- source: Kubernetes Job (batch/v1)\n  url: https://kubernetes.io/docs/concepts/workloads/controllers/job/\n  notes: "Kubernetes Jobs model the same \\"run-once, report status, possibly resume\\"\\\n    \\ lifecycle. Our kind \\u2248 spec.template.spec.containers[].image; config \\u2248\\\n    \\ spec.template.spec."\n',
    'leg': 'plural: legs\nsubtitle: flightNumber\nfields:\n  sequence: integer\n  departureTime: datetime\n  arrivalTime: datetime\n  duration: string\n  durationMinutes: integer\n  flightNumber: string\n  cabinClass: string\n  vehicleType: string\n  layoverMinutes: integer\n  carbonEmissions: json\n  trace: json\n  tracePointCount: integer\n  polyline: string\nrelations:\n  origin: place\n  destination: place\n  carrier: organization\n  aircraft: aircraft\n  trip: trip\nprior_art:\n- source: IATA NDC "segment"\n  url: https://www.iata.org/en/programs/airline-distribution/retailing/ndc/\n  notes: NDC segment = our leg. flightNumber, departureTime, arrivalTime, cabinClass\n    come straight from NDC OfferItem Segment.\n- source: GTFS stop_times.txt\n  url: https://gtfs.org/documentation/schedule/reference/#stop_timestxt\n  notes: Transit leg model. Our sequence = stop_sequence; departureTime/ arrivalTime\n    = arrival_time/departure_time.\n- source: Google Encoded Polyline Algorithm\n  url: https://developers.google.com/maps/documentation/utilities/polylinealgorithmformat\n  notes: Our polyline field is the standard Google encoded polyline. trace is a denser\n    GPS breadcrumb alternative (GeoJSON-adjacent).\n',
    'list': 'plural: lists\nidentity:\n- at\n- id\nfields:\n  listId: string\n  privacy: string\n  listType: string\n  isDefault: boolean\n  isPublic: boolean\nrelations:\n  at: actor\n  belongsTo: account\n  contains: product[]\nprior_art:\n- source: schema.org/ItemList\n  url: https://schema.org/ItemList\n  notes: "Our listType \\u2248 itemListOrder; contains \\u2248 itemListElement; isPublic\\\n    \\ \\u2248 publicAccess."\n- source: ActivityStreams 2.0 Collection / OrderedCollection\n  url: https://www.w3.org/TR/activitystreams-vocabulary/#dfn-collection\n  notes: "Our contains[] \\u2248 items; isDefault has no AS2 peer (platform-level concept)."\n',
    'loaded_model': 'plural: loaded_models\nsubtitle: size\nfields:\n  size: string\n  quantization: string\n  expiresAt: datetime\n  vramUsage: string\n  sizeVram: integer\n  digest: string\nprior_art:\n- source: "Ollama API \\u2014 /api/ps"\n  url: https://github.com/ollama/ollama/blob/main/docs/api.md#list-running-models\n  notes: Direct source. Our size/vramUsage/sizeVram/quantization/digest/ expiresAt\n    map to Ollama\'s ListRunningModelsResponse fields.\n- source: OpenTelemetry Resource semconv (ML/AI)\n  url: https://opentelemetry.io/docs/specs/semconv/gen-ai/\n  notes: Emerging conventions for GenAI observability. Our size/digest align with\n    gen_ai.model.* resource attributes.\n',
    'mcp_session': 'plural: mcp_sessions\nidentity:\n- client\n- projectId\n- gitBranch\nsubtitle: client\nicon: terminal\nfields:\n  client: string\n  projectId: string\n  gitBranch: string\n  sessionType: string\n  startedAt: datetime\n  endedAt: datetime\n  messageCount: integer\n  tokenCount: integer\nrelations:\n  participant: actor\n  folder: folder\nprior_art:\n- source: Model Context Protocol (MCP) session\n  url: https://modelcontextprotocol.io/specification\n  notes: Direct source. Our client/sessionType come from MCP\'s client/transport concepts\n    (STDIO, HTTP+SSE).\n- source: "OpenTelemetry Spans (root span \\u2248 session)"\n  url: https://opentelemetry.io/docs/concepts/signals/traces/\n  notes: Our startedAt/endedAt/messageCount/tokenCount align with span lifecycle +\n    attributes in a trace context.\n- source: OpenID Connect Session Management 1.0\n  url: https://openid.net/specs/openid-connect-session-1_0.html\n  notes: "Classical web-session model. Our participant \\u2248 authenticated subject;\\\n    \\ projectId/gitBranch are AgentOS-specific scoping."\n',
    'meeting': 'plural: meetings\nsubtitle: location\nalso:\n- event\nfields:\n  calendarLink: url\n  isVirtual: boolean\n  meetingUrl: url\n  conferenceProvider: string\n  phoneDialIn: string\nrelations:\n  transcribe: transcript\nprior_art:\n- source: RFC 5545 VEVENT + conference property (RFC 7986)\n  url: https://datatracker.ietf.org/doc/html/rfc7986#section-5.11\n  notes: "Our meetingUrl \\u2248 CONFERENCE URI; phoneDialIn = tel: URI in CONFERENCE\\\n    \\ feature=PHONE; conferenceProvider \\u2248 CONFERENCE LABEL."\n- source: "schema.org/Event \\u2014 location.VirtualLocation"\n  url: https://schema.org/VirtualLocation\n  notes: "Our isVirtual triggers VirtualLocation; meetingUrl \\u2248 VirtualLocation.url."\n- source: Google Calendar Event conferenceData\n  url: https://developers.google.com/calendar/api/v3/reference/events\n  notes: "Practical API mirror. Our conferenceProvider \\u2248 conferenceData.conferenceSolution.name;\\\n    \\ meetingUrl = entryPoints[uri]."\n',
    'memex': 'plural: memex\nsubtitle: description\nicon: brain\nfields:\n  description: text\n  origin: string\n  filePath: string\n  nodeCount: integer\n  edgeCount: integer\n  fileSize: string\n  snapshotOf: datetime\n  published: boolean\nrelations:\n  owner: person\n  forkedFrom: memex\n  snapshots: memex[]\nprior_art:\n- source: "Vannevar Bush \\u2014 \\"As We May Think\\" (1945)"\n  url: https://www.theatlantic.com/magazine/archive/1945/07/as-we-may-think/303881/\n  notes: The original concept. Our memex is named after and modeled on Bush\'s personal\n    knowledge store with associative trails.\n- source: W3C RDF 1.1 + Named Graphs\n  url: https://www.w3.org/TR/rdf11-concepts/\n  notes: "Formal underpinning. Our nodeCount/edgeCount mirror RDF subject-predicate-object\\\n    \\ triples; snapshots \\u2248 named-graph versioning."\n- source: Roam Research / Obsidian / Logseq PKM model\n  url: https://obsidian.md/\n  notes: Practical modern precedents. Our origin values (personal, domain, fork) generalize\n    the single-user PKM model to shareable graphs.\n',
    'message': 'plural: messages\nidentity:\n- at\n- id\nsubtitle: from\nfields:\n  isOutgoing: boolean\n  isStarred: boolean\nrelations:\n  at: actor\n  from: actor\n  inConversation: conversation\n  repliesTo: message\n  toolCalls: tool_call[]\nprior_art:\n- source: ActivityStreams 2.0 Note/Activity\n  url: https://www.w3.org/TR/activitystreams-vocabulary/#dfn-note\n  notes: "Closest open standard for generic messages. Our from \\u2248 actor; inConversation\\\n    \\ \\u2248 context/conversation; repliesTo \\u2248 inReplyTo."\n- source: Matrix m.room.message\n  url: https://spec.matrix.org/latest/client-server-api/#mroommessage\n  notes: "Practical cross-platform message event schema. Our isOutgoing has no Matrix\\\n    \\ analog (sender identity instead); repliesTo \\u2248 m.relates_to rel_type m.thread/m.in_reply_to."\n- source: XMPP (RFC 6121) message stanza\n  url: https://datatracker.ietf.org/doc/html/rfc6121\n  notes: IETF instant-messaging baseline. from/to/thread correspond to our from/inConversation;\n    no standardized isStarred.\n',
    'model': "plural: models\nidentity:\n- at\n- name\nsubtitle: name\nfields:\n  contextLength: integer\n  contextWindow: integer\n  maxOutput: integer\n  pricingInput: string\n  pricingOutput: string\n  modality: string[]\n  modelType: string\n  quantization: string\n  quantizationLevel: string\n  size: string\n  parameterSize: string\n  format: string\n  family: string\n  digest: string\nrelations:\n  at: actor\nprior_art:\n- source: Hugging Face Model Cards\n  url: https://huggingface.co/docs/hub/en/model-cards\n  notes: Our provider/contextLength/modality/family/quantization/ parameterSize align\n    with HF model-card metadata conventions.\n- source: Ollama /api/show + Modelfile\n  url: https://github.com/ollama/ollama/blob/main/docs/modelfile.md\n  notes: Our quantization/quantizationLevel/format/digest/parameterSize come directly\n    from Ollama's show-model response.\n- source: OpenRouter Models API\n  url: https://openrouter.ai/docs/models\n  notes: Our contextLength/contextWindow/maxOutput/pricingInput/ pricingOutput mirror\n    OpenRouter's model spec.\n",
    'note': 'plural: notes\nfields:\n  noteType: string\n  isPinned: boolean\nrelations:\n  createdBy: person\n  references: note[]\n  extractedFrom: webpage\nprior_art:\n- source: Zettelkasten / Luhmann slip-box\n  url: https://zettelkasten.de/overview/\n  notes: "Our noteType (fleeting/literature/permanent) is the canonical Zettelkasten\\\n    \\ triad; references[] \\u2248 Luhmann\'s permanent links."\n- source: W3C Web Annotation Data Model\n  url: https://www.w3.org/TR/annotation-model/\n  notes: Our extractedFrom = target; createdBy = creator. Notes are annotations without\n    a structured position selector.\n- source: Obsidian / Roam / Logseq PKM conventions\n  url: https://obsidian.md/\n  notes: Practical PKM lineage. isPinned/noteType mirror the "pinned/daily/permanent"\n    UX of modern note apps.\n',
    'offer': 'plural: offers\nfields:\n  price: number\n  currency: string\n  offerType: string\n  availability: string\n  validFrom: datetime\n  validUntil: datetime\n  bookingToken: string\nrelations:\n  for: product\n  offeredBy: organization\n  trips: trip[]\nprior_art:\n- source: schema.org/Offer\n  url: https://schema.org/Offer\n  notes: Our price = price; currency = priceCurrency; availability = availability;\n    validFrom/validUntil match directly.\n- source: IATA NDC OfferItem\n  url: https://www.iata.org/en/programs/airline-distribution/retailing/ndc/\n  notes: "Our bookingToken \\u2248 OfferItemID; validUntil \\u2248 TimeLimits/ OfferExpirationDateTime;\\\n    \\ trips[] \\u2248 Itinerary."\n- source: schema.org/AggregateOffer\n  url: https://schema.org/AggregateOffer\n  notes: For price-range offers (SerpAPI flight results). offerType is AgentOS-specific.\n',
    'order': 'plural: orders\nidentity:\n- at\n- orderId\nsubtitle: total\nfields:\n  orderId: string\n  orderDate: datetime\n  total: string\n  totalAmount: number\n  originalTotal: string\n  originalTotalAmount: number\n  savings: number\n  currency: string\n  status: string\n  deliveryDate: datetime\n  eta: string\n  subtotal: number\n  tipAmount: number\n  deliveryFee: number\n  taxes: number\n  summary: string\n  fareBreakdown: json\nrelations:\n  at: actor\n  contains: product[]\n  shippingAddress: place\n  store: place\n  delivery: trip\n  tracking: webpage\nprior_art:\n- source: schema.org/Order\n  url: https://schema.org/Order\n  notes: Our orderId = orderNumber; orderDate = orderDate; total = totalPaymentDue;\n    status = orderStatus; shippingAddress = orderDelivery.\n- source: schema.org/OrderStatus (enum)\n  url: https://schema.org/OrderStatus\n  notes: Our status values (placed, confirmed, delivering, completed, cancelled) map\n    to OrderProcessing/OrderInTransit/OrderDelivered/ OrderCancelled.\n- source: Amazon Order Reports (MWS / SP-API)\n  url: https://developer-docs.amazon.com/sp-api/docs/orders-api-v0-reference\n  notes: Practical source. Our orderId, fareBreakdown, savings, eta are lifted from\n    Amazon/Uber Eats order structures.\n',
    'organization': 'plural: organizations\nidentity: url\nsubtitle: industry\nalso:\n- actor\nfields:\n  industry: string\n  founded: datetime\nrelations:\n  member: person[]\n  domain: domain\n  website: website\n  headquarters: place\nprior_art:\n- source: schema.org/Organization\n  url: https://schema.org/Organization\n  notes: "Our industry \\u2248 naics/isicV4 (loosely); founded = foundingDate; member[]\\\n    \\ = member; headquarters = location (or subOrganization with a Place)."\n- source: vCard 4.0 KIND=org (RFC 6350)\n  url: https://datatracker.ietf.org/doc/html/rfc6350\n  notes: "Organization-as-contact. Our website/domain \\u2248 URL; headquarters \\u2248\\\n    \\ ADR. Thinner than schema.org for industry/founded."\n- source: Wikidata (Organization, Q43229)\n  url: https://www.wikidata.org/wiki/Q43229\n  notes: Cross-reference identity. Useful for deduping; no direct field alignment\n    but industry maps to P452 (industry) and founded to P571 (inception).\n',
    'person': 'plural: people\nsubtitle: about\nalso:\n- actor\nfields:\n  firstName: string\n  lastName: string\n  middleName: string\n  nickname: string\n  birthday: datetime\n  notes: text\n  gender: string\n  about: text\n  joinedDate: datetime\n  lastActive: datetime\nrelations:\n  accounts: account[]\n  roles: role[]\n  location: place\n  website: website\nprior_art:\n- source: schema.org/Person\n  url: https://schema.org/Person\n  notes: Our firstName/lastName = givenName/familyName; nickname = additionalName/alternateName;\n    birthday = birthDate; about = description. We diverge by modeling accounts[] as\n    a first-class relation rather than sameAs URLs.\n- source: vCard 4.0 (RFC 6350)\n  url: https://datatracker.ietf.org/doc/html/rfc6350\n  notes: "Contact-card canonical. Our fields map to FN/N/NICKNAME/BDAY/NOTE; our accounts[]\\\n    \\ \\u2248 IMPP/X-SOCIALPROFILE; location \\u2248 ADR."\n- source: FOAF (Friend of a Friend)\n  url: http://xmlns.com/foaf/spec/\n  notes: "Original social-graph vocabulary. foaf:Person with givenName/familyName/nick/homepage;\\\n    \\ foaf:account \\u2248 our accounts[]. Largely superseded by schema.org but still\\\n    \\ a reference for account-centric modeling."\n',
    'place': 'plural: places\nidentity_any:\n- googlePlaceId\n- mapboxId\nsubtitle: fullAddress\nfields:\n  fullAddress: string\n  placeFormatted: string\n  streetNumber: string\n  street: string\n  neighborhood: string\n  locality: string\n  city: string\n  district: string\n  region: string\n  postalCode: string\n  country: string\n  countryCode: string\n  latitude: number\n  longitude: number\n  accuracy: string\n  featureType: string\n  categories: string[]\n  phone: string\n  website: url\n  hours: json\n  businessStatus: string\n  rating: number\n  reviewCount: integer\n  priceLevel: string\n  timezone: string\n  mapboxId: string\n  wikidataId: string\n  googlePlaceId: string\nrelations:\n  brand: organization\n  offers: product[]\nprior_art:\n- source: schema.org/Place + PostalAddress\n  url: https://schema.org/Place\n  notes: "Our latitude/longitude = geo.latitude/longitude; street/city/region/postalCode/countryCode\\\n    \\ map to PostalAddress streetAddress/addressLocality/addressRegion/postalCode/addressCountry;\\\n    \\ hours \\u2248 openingHoursSpecification; rating/reviewCount \\u2248 aggregateRating."\n- source: Google Places API (Place resource)\n  url: https://developers.google.com/maps/documentation/places/web-service/reference/rest/v1/places\n  notes: "Practical POI schema. Our googlePlaceId = id; featureType/categories \\u2248\\\n    \\ types/primaryType; businessStatus, priceLevel, rating match directly."\n- source: GeoJSON (RFC 7946) + ISO 3166-1\n  url: https://datatracker.ietf.org/doc/html/rfc7946\n  notes: Our latitude/longitude are a GeoJSON Point [lon, lat]; countryCode follows\n    ISO 3166-1 alpha-2.\n',
    'playlist': 'plural: playlists\nsubtitle: text\nalso:\n- list\nrelations:\n  contains: video[]\nprior_art:\n- source: schema.org/MusicPlaylist / ItemList\n  url: https://schema.org/MusicPlaylist\n  notes: "Our contains(video[]) \\u2248 track/itemListElement. We generalize beyond\\\n    \\ music to any ordered media list."\n- source: "YouTube Data API \\u2014 Playlist"\n  url: https://developers.google.com/youtube/v3/docs/playlists\n  notes: "Practical source. Playlist = ordered Video collection \\u2014 inherits list\\\n    \\ identity semantics."\n',
    'podcast': 'plural: podcasts\nidentity:\n- at\n- id\nsubtitle: author\nfields:\n  feedUrl: url\nrelations:\n  host: person[]\n  at: actor\n  episode: episode[]\nprior_art:\n- source: RSS 2.0 (feed + channel)\n  url: https://www.rssboard.org/rss-specification\n  notes: "Our feedUrl is a canonical RSS feed URL; episodes relation \\u2248 channel\'s\\\n    \\ item elements."\n- source: Apple Podcasts RSS extensions (itunes:*)\n  url: https://help.apple.com/itc/podcasts_connect/#/itcb54353390\n  notes: "De-facto standard. Our host[] \\u2248 itunes:author; our series-episode hierarchy\\\n    \\ aligns with itunes:episode/itunes:season."\n- source: Podcast Namespace (podcast:*)\n  url: https://podcastindex.org/namespace/1.0\n  notes: Modern open extension. podcast:person covers guests/hosts; podcast:transcript\n    covers our transcribe relation.\n',
    'post': 'plural: posts\nidentity:\n- at\n- id\nsubtitle: author\nfields:\n  externalUrl: url\n  postType: string\nrelations:\n  postedBy: account\n  publish: community\n  repliesTo: post\n  replies: post[]\n  contains: video[]\n  media: image[]\n  attachment: file[]\nprior_art:\n- source: ActivityStreams 2.0 (Note/Article + Create)\n  url: https://www.w3.org/TR/activitystreams-vocabulary/\n  notes: "Fediverse post model. Our postedBy \\u2248 actor/attributedTo; publish(community)\\\n    \\ \\u2248 audience/to; repliesTo/replies \\u2248 inReplyTo/replies; media/attachment\\\n    \\ \\u2248 attachment."\n- source: OpenGraph protocol\n  url: https://ogp.me/\n  notes: How posts surface when linked. Our externalUrl + media[] correspond to og:url\n    and og:image/og:video; postType loosely parallels og:type (article, video).\n- source: ATProto app.bsky.feed.post\n  url: https://atproto.com/lexicons/app-bsky-feed\n  notes: "Modern practical lexicon. Our repliesTo \\u2248 reply.parent; media \\u2248\\\n    \\ embed.images; externalUrl \\u2248 embed.external."\n',
    'product': "plural: products\nsubtitle: brand\nfields:\n  category: string\n  price: string\n  priceAmount: number\n  originalPrice: string\n  originalPriceAmount: number\n  currency: string\n  categories: string[]\n  availability: string\n  images: json\n  quantity: integer\n  weight: string\n  weightValue: number\n  weightUnit: string\n  soldByWeight: boolean\n  department: string\n  aisle: string\n  sku: string\n  barcode: string\n  nutritionScore: string\n  novaGroup: integer\n  calories: number\n  servingSize: string\nrelations:\n  brand: brand\n  manufacturer: organization\n  tagged: tag[]\nprior_art:\n- source: schema.org/Product + Offer\n  url: https://schema.org/Product\n  notes: Product on schema.org, price/priceAmount/currency/availability on nested\n    Offer. Our sku/barcode map to sku/gtin13/gtin12; brand/manufacturer match directly.\n- source: GS1 GTIN (UPC/EAN)\n  url: https://www.gs1.org/standards/id-keys/gtin\n  notes: Canonical barcode standard. Our barcode field is a GTIN-8/12/13/14; GS1 also\n    underlies schema.org's gtin* properties.\n- source: Open Food Facts API\n  url: https://openfoodfacts.github.io/openfoodfacts-server/api/\n  notes: Best practical source for food attributes. Our nutritionScore/novaGroup/calories/servingSize\n    mirror nutriscore_grade/nova_group/nutriments.energy-kcal/serving_size.\n",
    'project': 'plural: projects\nidentity:\n- at\n- id\nsubtitle: state\nfields:\n  state: string\n  color: string\nprior_art:\n- source: "Linear API \\u2014 Project"\n  url: https://developers.linear.app/docs/graphql/working-with-the-graphql-api\n  notes: Our state/color come directly from Linear\'s Project model.\n- source: GitHub Projects (v2)\n  url: https://docs.github.com/en/graphql/reference/objects#projectv2\n  notes: "Canonical open-source project-board model. state \\u2248 ProjectV2SingleSelectFieldOption;\\\n    \\ color is per-field metadata."\n- source: schema.org/Project\n  url: https://schema.org/Project\n  notes: Generic project-as-effort type. Thinner than the practical APIs; mainly useful\n    for outbound JSON-LD.\n',
    'protocol': 'plural: protocols\nidentity:\n- name\nsubtitle: name\nfields:\n  name: string\n  homepage: url\n  rfc: string\n  wikidataId: string\nprior_art:\n- source: schema.org/CreativeWork\n  url: https://schema.org/CreativeWork\n  notes: "Closest match in schema.org \\u2014 protocols are creative works in the broadest\\\n    \\ sense. We narrow to protocols and technical specifications used as identity\\\n    \\ namespaces."\n- source: Wikidata (Communication protocol, Q15836568)\n  url: https://www.wikidata.org/wiki/Q15836568\n  notes: wikidataId enables cross-reference for dedupe across other knowledge graphs.\n    Most well-known protocols have Q-IDs.\n- source: IANA Protocol Registry\n  url: https://www.iana.org/protocols\n  notes: Authoritative registry for many protocols. Our `name` aligns with IANA protocol\n    slugs where applicable.\n',
    'quote': 'plural: quotes\nfields:\n  context: string\n  year: integer\nprior_art:\n- source: schema.org/Quotation\n  url: https://schema.org/Quotation\n  notes: "Our context \\u2248 about; year \\u2248 datePublished. schema.org models spokenByCharacter/creator\\\n    \\ \\u2014 we model attribution via graph edges instead."\n- source: Wikiquote data model\n  url: https://en.wikiquote.org/wiki/Help:Sources\n  notes: Practical canonical quote source. Our provenance-via-edges (document --contains-->\n    quote --attributedTo--> person) matches Wikiquote\'s source-citation discipline.\n',
    'repository': 'plural: repositories\nidentity_any:\n- path\n- url\nsubtitle: language\nfields:\n  stars: integer\n  forks: integer\n  language: string\n  topics: string[]\n  openIssues: integer\n  isArchived: boolean\n  isPrivate: boolean\n  defaultBranch: string\n  license: string\n  size: integer\nrelations:\n  forkedFrom: repository\n  owner: account\nprior_art:\n- source: Git internals + Git refs\n  url: https://git-scm.com/book/en/v2/Git-Internals-Git-References\n  notes: Our defaultBranch is a Git ref (refs/heads/main); forkedFrom is explicit\n    in our model vs. implicit in Git (recorded only by forges).\n- source: "GitHub REST API \\u2014 Repository"\n  url: https://docs.github.com/en/rest/repos/repos\n  notes: Direct source. Our stars/forks/openIssues/topics/defaultBranch/ license/size/isArchived/isPrivate\n    all come from the GitHub Repository resource.\n- source: SPDX License List\n  url: https://spdx.org/licenses/\n  notes: Our license values are SPDX identifiers (MIT, Apache-2.0, GPL-3.0-or-later).\n',
    'result': 'plural: results\nsubtitle: url\nfields:\n  indexedAt: datetime\n  resultType: string\nprior_art:\n- source: OpenSearch Description Document\n  url: https://github.com/dewitt/opensearch/blob/master/opensearch-1-1-draft-6.md\n  notes: "Result-pointer model: each hit has a URL + metadata. Our resultType \\u2248\\\n    \\ Url template\'s type attribute."\n- source: Web Search API conventions (Brave/Bing)\n  url: https://api.search.brave.com/app/documentation/web-search/get-started\n  notes: Practical source. Our indexedAt/resultType align with common fields across\n    Brave, Bing, and Exa web APIs.\n',
    'review': 'plural: reviews\nsubtitle: author\nalso:\n- post\nfields:\n  rating: number\n  ratingMax: number\n  tags: string[]\n  isVerified: boolean\nrelations:\n  reviews: product\n  postedBy: account\nprior_art:\n- source: schema.org/Review\n  url: https://schema.org/Review\n  notes: "Our rating \\u2248 reviewRating.ratingValue; ratingMax \\u2248 bestRating;\\\n    \\ reviews = itemReviewed; isVerified has no direct property (extension)."\n- source: schema.org/AggregateRating\n  url: https://schema.org/AggregateRating\n  notes: For product review aggregates. Our rating/ratingMax map to ratingValue/bestRating;\n    reviewCount is inherited when computed.\n',
    'role': 'plural: roles\nsubtitle: name\nfields:\n  title: string\n  department: string\n  roleType: string\n  startDate: datetime\n  endDate: datetime\nrelations:\n  person: person\n  organization: organization\nprior_art:\n- source: schema.org/Role + OrganizationRole\n  url: https://schema.org/OrganizationRole\n  notes: "Our title = roleName; startDate/endDate match; department \\u2248 name of\\\n    \\ a subOrganization; person/organization = Role\'s nested pattern."\n- source: FOAF + Bio vocabularies (position)\n  url: http://vocab.org/bio/0.1/.html\n  notes: "Period-of-employment modeling. Our startDate/endDate \\u2248 bio:date; roleType\\\n    \\ has no FOAF peer."\n',
    'search': 'plural: searches\nidentity:\n- query\nsubtitle: query\nicon: magnifying-glass\nfields:\n  query: string\n  searchedAt: datetime\n  searchCount: integer\n  resultCount: integer\nprior_art:\n- source: OpenSearch Description (Url templates)\n  url: https://github.com/dewitt/opensearch/blob/master/opensearch-1-1-draft-6.md\n  notes: "Our query field is the searchTerm in OpenSearch\'s Url template. resultCount\\\n    \\ \\u2248 totalResults header."\n- source: schema.org/SearchAction\n  url: https://schema.org/SearchAction\n  notes: "Our query + searchedAt \\u2248 SearchAction.query + startTime. searchCount\\\n    \\ is AgentOS-specific (reuse telemetry)."\n',
    'shelf': 'plural: shelves\nalso:\n- list\nfields:\n  isExclusive: boolean\nrelations:\n  contains: book[]\nprior_art:\n- source: "Goodreads API \\u2014 Shelves"\n  url: https://www.goodreads.com/api\n  notes: Direct source. Our isExclusive maps to Goodreads\' "exclusive shelves" (read,\n    to-read, currently-reading).\n- source: schema.org/ItemList (bookshelf)\n  url: https://schema.org/ItemList\n  notes: "Generic collection peer. contains(book[]) \\u2248 itemListElement."\n',
    'shortcut': 'plural: shortcuts\nidentity:\n- name\nsubtitle: target\nicon: link\nfields:\n  name: string\n  target: string\n  filter: string\n  builtin: boolean\nrelations:\n  skill: skill\nprior_art:\n- source: Unix shell aliases (bash/zsh)\n  url: https://pubs.opengroup.org/onlinepubs/9699919799/utilities/alias.html\n  notes: "Our name\\u2192target expansion follows the alias pattern. builtin vs user-created\\\n    \\ parallels shell builtins vs. rc-file aliases."\n- source: "Vannevar Bush \\u2014 \\"As We May Think\\" (1945, associative trails)"\n  url: https://www.theatlantic.com/magazine/archive/1945/07/as-we-may-think/303881/\n  notes: Named trails through the memex. Our named shortcut-to-URI mapping is a mechanized\n    version of Bush\'s trail idea.\n- source: RFC 3986 URI Generic Syntax\n  url: https://datatracker.ietf.org/doc/html/rfc3986\n  notes: Our target is a URI (location URI). Shortcut names resolve to RFC 3986-compliant\n    references.\n',
    'simulation': 'plural: simulations\nsubtitle: status\nicon: shield\nfields:\n  status: string\n  profile: string\n  task: text\n  graphMode: string\n  startedAt: datetime\n  endedAt: datetime\n  actionCount: integer\n  writeCount: integer\nrelations:\n  primaryMemex: memex\n  mountedMemex: memex[]\n  agent: agent\n  tether: hardware\n  forkedFrom: simulation\n  startedBy: person\nprior_art:\n- source: OpenTelemetry Traces (root span + attributes)\n  url: https://opentelemetry.io/docs/concepts/signals/traces/\n  notes: "Span-shaped observation of an agent run. Our startedAt/endedAt/ actionCount/writeCount\\\n    \\ \\u2248 span attributes; status \\u2248 span status."\n- source: QEMU / VM snapshots\n  url: https://qemu-project.gitlab.io/qemu/system/images.html\n  notes: "\\"Disk image vs. VM\\" metaphor is direct. Our primaryMemex \\u2248 writable\\\n    \\ disk; mountedMemex[] \\u2248 read-only overlays; forkedFrom \\u2248 snapshot-based\\\n    \\ fork."\n- source: Kubernetes Pod + Volume mounts\n  url: https://kubernetes.io/docs/concepts/workloads/pods/\n  notes: "Our tether (hardware kill-switch) \\u2248 Pod security context; mountedMemex[]\\\n    \\ \\u2248 ConfigMap/PVC read-only mounts."\n',
    'skill': 'plural: skills\nsubtitle: description\nfields:\n  skillId: string\n  description: text\n  color: string\n  status: string\n  error: text\nrelations:\n  website: website\n  privacyPolicy: webpage\n  termsOfService: webpage\nprior_art:\n- source: "Model Context Protocol (MCP) \\u2014 Server"\n  url: https://modelcontextprotocol.io/specification\n  notes: "Our skill = an MCP-registerable capability provider. skillId \\u2248 MCP\\\n    \\ server name; status tracks connection lifecycle."\n- source: OpenAPI 3.1 (Info + Servers)\n  url: https://spec.openapis.org/oas/v3.1.0\n  notes: "Our description/website/privacyPolicy/termsOfService \\u2248 OpenAPI info.description/info.termsOfService/info.license/contact."\n- source: Anthropic Tool Use (skills-as-tools)\n  url: https://docs.anthropic.com/en/docs/build-with-claude/tool-use\n  notes: Each AgentOS skill publishes tools consumed via MCP/Tool-Use. status/error\n    surface tool-call health back to the agent.\n',
    'software': 'plural: software\nidentity: url\nsubtitle: text\nalso:\n- product\nfields:\n  version: string\n  license: string\n  platform: string[]\n  openSource: boolean\n  repositoryUrl: url\nrelations:\n  developer: organization\n  repository: repository\nprior_art:\n- source: schema.org/SoftwareApplication\n  url: https://schema.org/SoftwareApplication\n  notes: "Our version = softwareVersion; license matches; platform[] \\u2248 operatingSystem;\\\n    \\ developer = creator/author."\n- source: SPDX License List\n  url: https://spdx.org/licenses/\n  notes: Our license values are canonical SPDX identifiers.\n- source: schema.org/SoftwareSourceCode\n  url: https://schema.org/SoftwareSourceCode\n  notes: "Our repositoryUrl \\u2248 codeRepository; openSource implied by SPDX-license\\\n    \\ + codeRepository presence."\n',
    'source': 'plural: sources\nidentity: address\nsubtitle: sourceId\nicon: "\\U0001F4E6"\nfields:\n  sourceId: string\n  address: string\n  scanner: string\n  enabled: boolean\n  description: text\n  lastSynced: datetime\nrelations:\n  folder: folder\nprior_art:\n- source: Homebrew Taps\n  url: https://docs.brew.sh/Taps\n  notes: Direct precedent. Our sourceId/address match tap name/URL; our platform=agentos\n    parallels tap formulae discovery.\n- source: Cydia / Sileo (APT repos for iOS)\n  url: https://wiki.theapebox.com/index.php/Package_Management\n  notes: Namespaced third-party source model. Our sourceId prefix is the Cydia repo-namespace\n    pattern.\n- source: Debian APT sources.list\n  url: https://wiki.debian.org/SourcesList\n  notes: "Canonical third-party source mechanism. Our enabled flag parallels APT source\\\n    \\ enable/disable; lastSynced \\u2248 apt-get update timestamp."\n',
    'spec': 'plural: specs\nsubtitle: state\nalso:\n- task\n- file\nfields:\n  problem: text\n  successCriteria: text\nrelations:\n  dependsOn: spec[]\n  supersedes: spec[]\nprior_art:\n- source: IETF RFC process\n  url: https://www.ietf.org/standards/rfcs/\n  notes: Canonical "design doc with problem statement and success criteria" lineage.\n    Our problem/successCriteria mirror the RFC structure.\n- source: Architectural Decision Records (ADR / MADR)\n  url: https://adr.github.io/\n  notes: Modern in-repo equivalent. supersedes[] matches ADR\'s "Supersedes" link;\n    dependsOn[] has no direct ADR peer.\n- source: Python PEP (spec-as-markdown)\n  url: https://peps.python.org/pep-0001/\n  notes: PEP states problem, rationale, spec, rejected alternatives. Our fields are\n    a slim version of the PEP template.\n',
    'tag': 'plural: tags\nsubtitle: tagType\nfields:\n  color: string\n  tagType: string\nprior_art:\n- source: "GitHub REST API \\u2014 Labels"\n  url: https://docs.github.com/en/rest/issues/labels\n  notes: "Our color/name/tagType \\u2248 GitHub Label\'s color/name/default."\n- source: "Gmail API \\u2014 Labels"\n  url: https://developers.google.com/gmail/api/reference/rest/v1/users.labels\n  notes: Practical source. Our tagType distinguishes Gmail\'s SYSTEM vs USER label\n    types.\n- source: Dublin Core dc:subject\n  url: https://www.dublincore.org/specifications/dublin-core/dces/\n  notes: "Generic classification vocabulary \\u2014 tags on any resource."\n',
    'task': 'plural: tasks\nidentity:\n- at\n- id\nsubtitle: state\nfields:\n  remoteId: string\n  priority: integer\n  state: string\n  labels: string[]\n  startedAt: datetime\n  targetDate: datetime\nrelations:\n  assignedTo: person\n  project: project\n  repository: repository\n  parent: task\n  children: task[]\n  blockedBy: task[]\n  blocks: task[]\nprior_art:\n- source: "GitHub REST API \\u2014 Issues"\n  url: https://docs.github.com/en/rest/issues/issues\n  notes: Direct source. Our remoteId/state/labels/assignedTo/parent/ children/blockedBy/blocks\n    map to GitHub Issue + sub-issues + task-list tracking.\n- source: "Linear GraphQL API \\u2014 Issue"\n  url: https://developers.linear.app/docs/graphql/working-with-the-graphql-api\n  notes: Practical canonical. Our priority/state/project/targetDate align with Linear\'s\n    Issue model exactly.\n- source: "Todoist REST API v2 \\u2014 Tasks"\n  url: https://developer.todoist.com/rest/v2/\n  notes: "Consumer-grade task model. Our startedAt/targetDate \\u2248 created_at/due;\\\n    \\ labels match directly."\n',
    'theme': 'plural: themes\nidentity: themeId\nsubtitle: family\nfields:\n  themeId: string\n  family: string\n  colorScheme: string\n  description: text\nrelations:\n  wallpaper: image\nprior_art:\n- source: CSS color-scheme (W3C CSS Color Adjustment)\n  url: https://www.w3.org/TR/css-color-adjust-1/#color-scheme-prop\n  notes: Our colorScheme = CSS color-scheme values (light/dark/both).\n- source: System theme APIs (macOS NSAppearance, Windows WinUI)\n  url: https://developer.apple.com/documentation/appkit/nsappearance\n  notes: OS-level theme abstraction. Our family parallels NSAppearance.Name (aqua,\n    darkAqua) and Windows theme families.\n',
    'tool_call': "plural: tool_calls\nidentity:\n- platform\n- id\nsubtitle: name\nfields:\n  name: string\n  input: text\n  output: text\n  isError: boolean\n  durationMs: integer\nrelations:\n  platform: product\n  from: actor\n  inMessage: message\n  repliesTo: tool_call\nprior_art:\n- source: Anthropic Tool Use API\n  url: https://docs.anthropic.com/en/docs/build-with-claude/tool-use\n  notes: Our name/input/output/isError map to tool_use/tool_result blocks in Claude's\n    message API.\n- source: OpenAI Function Calling / tool_calls\n  url: https://platform.openai.com/docs/guides/function-calling\n  notes: Our name/input = function.name/function.arguments; output is the tool-result\n    message content.\n- source: OpenTelemetry GenAI semconv\n  url: https://opentelemetry.io/docs/specs/semconv/gen-ai/\n  notes: Emerging observability standard. Our durationMs/isError align with gen_ai.tool.*\n    span attributes.\n",
    'transaction': 'plural: transactions\nidentity:\n- at\n- id\nsubtitle: category\nfields:\n  amount: number\n  currency: string\n  balance: number\n  category: string\n  postingDate: datetime\n  pending: boolean\n  recurring: boolean\n  notes: string\n  type: string\n  details: json\nrelations:\n  account: account\nprior_art:\n- source: OFX (Open Financial Exchange) STMTTRN\n  url: https://financialdataexchange.org/ofx\n  notes: Direct source. Our amount/type/postingDate/balance map to STMTTRN TRNAMT/TRNTYPE/DTPOSTED/BALAMT.\n- source: ISO 20022 payments messaging\n  url: https://www.iso20022.org/\n  notes: "Modern bank-messaging. Our currency = Ccy; category \\u2248 purpose code;\\\n    \\ details \\u2248 RemittanceInformation."\n- source: Plaid Transactions API\n  url: https://plaid.com/docs/api/products/transactions/\n  notes: Practical mirror. Our category/pending/recurring/notes match Plaid\'s category/pending/personal_finance_category/name\n    fields.\n',
    'transcript': 'plural: transcripts\nfields:\n  language: string\n  sourceType: string\n  contentRole: string\n  durationMs: integer\n  segmentCount: integer\n  segments: json\nprior_art:\n- source: WebVTT (W3C)\n  url: https://www.w3.org/TR/webvtt1/\n  notes: Our segments are WebVTT cues (start/end/text). language follows WebVTT\'s\n    LANGUAGE header.\n- source: SRT SubRip Subtitles\n  url: https://matroska.org/technical/subtitles.html#srt-subtitles\n  notes: Practical alternative cue format. Same segment shape.\n- source: Whisper JSON output\n  url: https://github.com/openai/whisper\n  notes: "Practical source \\u2014 many transcript skills return Whisper-shaped JSON\\\n    \\ (segments with start/end/text). Direct match."\n',
    'trip': 'plural: trips\nidentity:\n- at\n- id\nsubtitle: tripType\nfields:\n  tripType: string\n  status: string\n  departureTime: datetime\n  arrivalTime: datetime\n  duration: string\n  durationMinutes: integer\n  distance: string\n  vehicleType: string\n  cabinClass: string\n  fare: string\n  fareAmount: number\n  currency: string\n  rating: string\n  trackingUrl: url\n  isSurge: boolean\n  isScheduled: boolean\n  stops: integer\n  bookingToken: string\n  carbonEmissions: json\nrelations:\n  origin: place\n  destination: place\n  legs: leg[]\n  carrier: organization\n  driver: person\n  order: order\nprior_art:\n- source: schema.org/Trip + subTrip\n  url: https://schema.org/Trip\n  notes: "Our origin/destination/departureTime/arrivalTime map exactly; legs[] \\u2248\\\n    \\ subTrip or itinerary."\n- source: IATA NDC Slice (airline itineraries)\n  url: https://www.iata.org/en/programs/airline-distribution/retailing/ndc/\n  notes: NDC slice = our trip; NDC segment = our leg. cabinClass, bookingToken come\n    from NDC offer items.\n- source: "Uber API \\u2014 Trip resource"\n  url: https://developer.uber.com/docs/riders/references/api\n  notes: Practical source for ride trips. Our fare/fareAmount/ trackingUrl/isSurge/isScheduled\n    lifted from Uber\'s Trip model.\n',
    'video': 'plural: videos\nsubtitle: author\nalso:\n- file\nfields:\n  durationMs: integer\n  resolution: string\n  frameRate: number\n  codec: string\nrelations:\n  channel: channel\n  transcribe: transcript\n  addTo: playlist\nprior_art:\n- source: schema.org/VideoObject\n  url: https://schema.org/VideoObject\n  notes: "Our durationMs \\u2248 duration (ISO 8601 period); resolution \\u2248 videoFrameSize;\\\n    \\ frameRate has no direct property; codec \\u2248 encodingFormat."\n- source: IANA Media Types (video/*)\n  url: https://www.iana.org/assignments/media-types/media-types.xhtml#video\n  notes: Our codec values map to registered video/* media types (mp4, webm, ogg).\n- source: MPEG / ITU video codec specs\n  url: https://www.itu.int/rec/T-REC-H.264\n  notes: Canonical codec definitions. Our codec values are MPEG/ITU codec short names\n    (h264, vp9, av1).\n',
    'volume': 'plural: volumes\nsubtitle: path\nfields:\n  path: string\n  totalBytes: integer\n  freeBytes: integer\n  usedBytes: integer\n  filesystem: string\n  volumeType: string\n  removable: boolean\n  readOnly: boolean\nrelations:\n  contains: folder[]\nprior_art:\n- source: POSIX / Single Unix Specification (mount)\n  url: https://pubs.opengroup.org/onlinepubs/9699919799/functions/mount.html\n  notes: "Our path = mount point; filesystem \\u2248 fs type; readOnly \\u2248 ro mount\\\n    \\ option."\n- source: macOS DiskArbitration + diskutil\n  url: https://ss64.com/osx/diskutil.html\n  notes: Practical source. Our totalBytes/freeBytes/usedBytes/removable/ volumeType\n    match diskutil info output.\n- source: Linux /proc/mounts + statvfs\n  url: https://man7.org/linux/man-pages/man5/proc.5.html\n  notes: POSIX-family source. Our filesystem values (apfs, hfs+, ext4, ntfs) are standard\n    /proc/mounts fs-types.\n',
    'webpage': 'plural: webpages\nidentity: url\nsubtitle: url\nfields:\n  visitCount: integer\n  lastVisitUnix: integer\n  contentType: string\n  error: string\nprior_art:\n- source: schema.org/WebPage\n  url: https://schema.org/WebPage\n  notes: "Our URL-as-identity matches schema.org\'s @id/url convention; contentType\\\n    \\ \\u2248 encodingFormat."\n- source: HTTP semantics (RFC 9110)\n  url: https://datatracker.ietf.org/doc/html/rfc9110\n  notes: "Our contentType is the Content-Type response header; error \\u2248 non-2xx\\\n    \\ status text."\n- source: Chrome history / WebExtensions History API\n  url: https://developer.chrome.com/docs/extensions/reference/api/history\n  notes: Practical source. Our visitCount/lastVisitUnix lift from the history API\'s\n    VisitItem structure.\n',
    'website': 'plural: websites\nidentity: url\nsubtitle: url\nfields:\n  status: string\n  versionId: string\n  expiresAt: datetime\n  anonymous: boolean\n  claimToken: string\n  claimUrl: url\nrelations:\n  domain: domain\n  ownedBy: organization\nprior_art:\n- source: schema.org/WebSite\n  url: https://schema.org/WebSite\n  notes: "Our url-as-identity matches; ownedBy \\u2248 publisher; domain relation \\u2248\\\n    \\ url host."\n- source: WHOIS (RFC 3912)\n  url: https://datatracker.ietf.org/doc/html/rfc3912\n  notes: Our expiresAt/domain source from WHOIS records; claimToken has no direct\n    WHOIS peer (HERE.NOW-specific).\n- source: RFC 7033 WebFinger (host-meta)\n  url: https://datatracker.ietf.org/doc/html/rfc7033\n  notes: Website metadata discovery. Our claimUrl parallels /.well-known/host-meta\n    patterns.\n',
}

# Identity keys per shape — sidecars for the skill worker.
SHAPE_IDENTITIES: dict[str, list[str]] = {
    'account': ['at', 'identifier'],
    'aircraft': ['icaoCode'],
    'album': ['id'],
    'app': ['id'],
    'brand': ['url'],
    'calendar': ['at', 'calendarId'],
    'channel': ['at', 'id'],
    'community': ['at', 'id'],
    'conversation': ['at', 'id'],
    'dns_record': ['domain', 'recordType', 'recordName'],
    'domain': ['name'],
    'email': ['at', 'id'],
    'event': ['at', 'id'],
    'folder': ['path'],
    'group': ['at', 'id'],
    'hardware': ['serialNumber'],
    'invitation': ['at', 'id'],
    'job': ['name', 'boot_epoch'],
    'list': ['at', 'id'],
    'mcp_session': ['client', 'projectId', 'gitBranch'],
    'message': ['at', 'id'],
    'model': ['at', 'name'],
    'order': ['at', 'orderId'],
    'organization': ['url'],
    'podcast': ['at', 'id'],
    'post': ['at', 'id'],
    'project': ['at', 'id'],
    'protocol': ['name'],
    'search': ['query'],
    'shortcut': ['name'],
    'software': ['url'],
    'source': ['address'],
    'task': ['at', 'id'],
    'theme': ['themeId'],
    'tool_call': ['platform', 'id'],
    'transaction': ['at', 'id'],
    'trip': ['at', 'id'],
    'webpage': ['url'],
    'website': ['url'],
}

SHAPE_IDENTITIES_ANY: dict[str, list[str]] = {
    'book': ['isbn13', 'isbn'],
    'place': ['googlePlaceId', 'mapboxId'],
    'repository': ['path', 'url'],
}
