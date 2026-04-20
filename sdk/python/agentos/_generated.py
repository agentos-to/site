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
    session: Session


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


# Machine-readable shape definitions — consumed by the skill worker
# to attach `shape_def` on every @returns(shape) response.
# Shape-lazy Phase 2 (_roadmap/p1/shapes-lazy/proposal.md §3.1).
SHAPE_DEFS: dict[str, dict] = {
    'account': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'string',
            'datePublished': 'string',
            'content': 'string',
            'accountType': 'string',
            'bio': 'text',
            'color': 'string',
            'displayName': 'string',
            'email': 'string',
            'handle': 'string',
            'identifier': 'string',
            'isActive': 'boolean',
            'joinedDate': 'datetime',
            'lastActive': 'datetime',
            'phone': 'string',
            'at': 'actor',
            'authenticatedVia': 'account',
            'followers': 'account[]',
            'follows': 'account[]',
            'operator': 'actor',
            'owner': 'person',
            'previousIdentity': 'account[]',
            'protocol': 'protocol',
            'via': 'product',
        },
        'identity': ['at', 'identifier'],
        'also': [],
    },
    'activity': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'string',
            'datePublished': 'string',
            'content': 'string',
            'action': 'string',
            'changedKeys': 'string[]',
            'duration': 'number',
            'published': 'datetime',
            'success': 'boolean',
            'toolName': 'string',
            'folder': 'folder',
            'session': 'session',
        },
        'identity': [],
        'also': [],
    },
    'actor': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'string',
            'datePublished': 'string',
            'content': 'string',
            'actorType': 'string',
        },
        'identity': [],
        'also': [],
    },
    'agent': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'string',
            'datePublished': 'string',
            'content': 'string',
            'actorType': 'string',
            'model': 'string',
            'provider': 'string',
            'sessionId': 'string',
        },
        'identity': [],
        'also': ['actor'],
    },
    'aircraft': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'string',
            'datePublished': 'string',
            'content': 'string',
            'aisle': 'string',
            'availability': 'string',
            'barcode': 'string',
            'calories': 'number',
            'categories': 'string[]',
            'category': 'string',
            'currency': 'string',
            'department': 'string',
            'iataCode': 'string',
            'icaoCode': 'string',
            'images': 'json',
            'model': 'string',
            'novaGroup': 'integer',
            'nutritionScore': 'string',
            'originalPrice': 'string',
            'originalPriceAmount': 'number',
            'price': 'string',
            'priceAmount': 'number',
            'quantity': 'integer',
            'rangeKm': 'integer',
            'seatCapacity': 'integer',
            'servingSize': 'string',
            'sku': 'string',
            'soldByWeight': 'boolean',
            'variant': 'string',
            'weight': 'string',
            'weightUnit': 'string',
            'weightValue': 'number',
            'brand': 'brand',
            'manufacturer': 'organization',
            'tagged': 'tag[]',
        },
        'identity': ['icaoCode'],
        'also': ['product'],
    },
    'album': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'string',
            'datePublished': 'string',
            'content': 'string',
            'contains': 'image[]',
        },
        'identity': ['id'],
        'also': [],
    },
    'app': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'string',
            'datePublished': 'string',
            'content': 'string',
            'app_id': 'string',
            'description': 'string',
            'entity_types': 'json',
            'standalone': 'boolean',
        },
        'identity': ['id'],
        'also': [],
    },
    'book': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'string',
            'datePublished': 'string',
            'content': 'string',
            'aisle': 'string',
            'availability': 'string',
            'awardsWon': 'string[]',
            'barcode': 'string',
            'calories': 'number',
            'categories': 'string[]',
            'category': 'string',
            'characters': 'string[]',
            'currency': 'string',
            'department': 'string',
            'format': 'string',
            'genres': 'string[]',
            'images': 'json',
            'isbn': 'string',
            'isbn13': 'string',
            'language': 'string',
            'novaGroup': 'integer',
            'nutritionScore': 'string',
            'originalPrice': 'string',
            'originalPriceAmount': 'number',
            'originalTitle': 'string',
            'pages': 'integer',
            'places': 'string[]',
            'price': 'string',
            'priceAmount': 'number',
            'quantity': 'integer',
            'series': 'string',
            'servingSize': 'string',
            'sku': 'string',
            'soldByWeight': 'boolean',
            'weight': 'string',
            'weightUnit': 'string',
            'weightValue': 'number',
            'brand': 'brand',
            'contributors': 'person[]',
            'manufacturer': 'organization',
            'publisher': 'organization',
            'tagged': 'tag[]',
            'writtenBy': 'person',
        },
        'identity': ['isbn13', 'isbn'],
        'also': ['product'],
    },
    'branch': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'string',
            'datePublished': 'string',
            'content': 'string',
            'ahead': 'integer',
            'behind': 'integer',
            'commit': 'string',
            'isCurrent': 'boolean',
            'isRemote': 'boolean',
            'upstream': 'string',
            'repository': 'repository',
        },
        'identity': [],
        'also': [],
    },
    'brand': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'string',
            'datePublished': 'string',
            'content': 'string',
            'country': 'string',
            'founded': 'datetime',
            'tagline': 'string',
            'ownedBy': 'organization',
            'website': 'website',
        },
        'identity': ['url'],
        'also': [],
    },
    'calendar': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'string',
            'datePublished': 'string',
            'content': 'string',
            'accessRole': 'string',
            'backgroundColor': 'string',
            'calendarId': 'string',
            'color': 'string',
            'foregroundColor': 'string',
            'isPrimary': 'boolean',
            'isReadonly': 'boolean',
            'source': 'string',
            'timezone': 'string',
            'events': 'event[]',
            'owner': 'person',
        },
        'identity': ['at', 'calendarId'],
        'also': [],
    },
    'channel': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'string',
            'datePublished': 'string',
            'content': 'string',
            'banner': 'url',
            'at': 'actor',
        },
        'identity': ['at', 'id'],
        'also': [],
    },
    'class': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'string',
            'datePublished': 'string',
            'content': 'string',
            'activityType': 'string',
            'allDay': 'boolean',
            'capacity': 'integer',
            'dateUpdated': 'datetime',
            'endDate': 'datetime',
            'eventType': 'string',
            'icalUid': 'string',
            'isFull': 'boolean',
            'recurrence': 'string[]',
            'showAs': 'string',
            'sourceTitle': 'string',
            'sourceUrl': 'url',
            'spotsRemaining': 'integer',
            'startDate': 'datetime',
            'status': 'string',
            'timezone': 'string',
            'visibility': 'string',
            'at': 'actor',
            'attachments': 'file[]',
            'creator': 'person',
            'instructor': 'person',
            'involves': 'person[]',
            'location': 'place',
            'organizer': 'person',
            'venue': 'place',
        },
        'identity': [],
        'also': ['event'],
    },
    'community': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'string',
            'datePublished': 'string',
            'content': 'string',
            'privacy': 'string',
            'at': 'actor',
        },
        'identity': ['at', 'id'],
        'also': [],
    },
    'conversation': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'string',
            'datePublished': 'string',
            'content': 'string',
            'accountEmail': 'string',
            'cwd': 'string',
            'gitBranch': 'string',
            'isArchived': 'boolean',
            'isGroup': 'boolean',
            'messageCount': 'integer',
            'unreadCount': 'integer',
            'at': 'actor',
            'in': 'folder',
            'message': 'message[]',
            'participant': 'actor[]',
        },
        'identity': ['at', 'id'],
        'also': [],
    },
    'dns_record': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'string',
            'datePublished': 'string',
            'content': 'string',
            'domain': 'string',
            'recordName': 'string',
            'recordType': 'string',
            'ttl': 'integer',
            'values': 'string[]',
        },
        'identity': ['domain', 'recordType', 'recordName'],
        'also': [],
    },
    'document': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'actor',
            'datePublished': 'string',
            'content': 'string',
            'abstract': 'text',
            'contentType': 'string',
            'encoding': 'string',
            'filename': 'string',
            'format': 'string',
            'kind': 'string',
            'language': 'string',
            'lineCount': 'integer',
            'mimeType': 'string',
            'path': 'string',
            'sha': 'string',
            'size': 'integer',
            'tableOfContents': 'text',
            'wordCount': 'integer',
            'attachedTo': 'message',
            'citedBy': 'document[]',
            'references': 'document[]',
            'repository': 'repository',
        },
        'identity': [],
        'also': ['file'],
    },
    'domain': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'string',
            'datePublished': 'string',
            'content': 'string',
            'autoRenew': 'boolean',
            'expiresAt': 'datetime',
            'nameservers': 'string[]',
            'registrar': 'string',
            'status': 'string',
        },
        'identity': ['name'],
        'also': [],
    },
    'email': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'string',
            'datePublished': 'string',
            'content': 'string',
            'accountEmail': 'string',
            'attachments': 'json',
            'authResults': 'string',
            'bccRaw': 'string',
            'bodyHtml': 'text',
            'ccRaw': 'string',
            'deliveredTo': 'string',
            'hasAttachments': 'boolean',
            'inReplyTo': 'string',
            'isAutomated': 'boolean',
            'isDraft': 'boolean',
            'isOutgoing': 'boolean',
            'isSent': 'boolean',
            'isSpam': 'boolean',
            'isStarred': 'boolean',
            'isTrash': 'boolean',
            'isUnread': 'boolean',
            'listId': 'string',
            'mailer': 'string',
            'manageSubscription': 'string',
            'messageId': 'string',
            'precedence': 'string',
            'references': 'string',
            'replyTo': 'string',
            'returnPath': 'string',
            'sizeEstimate': 'integer',
            'subject': 'string',
            'toRaw': 'string',
            'unsubscribe': 'string',
            'unsubscribeOneClick': 'boolean',
            'at': 'actor',
            'bcc': 'account[]',
            'cc': 'account[]',
            'ccDomain': 'domain[]',
            'domain': 'domain',
            'from': 'account',
            'inConversation': 'conversation',
            'repliesTo': 'message',
            'tag': 'tag[]',
            'to': 'account[]',
            'toDomain': 'domain[]',
            'toolCalls': 'tool_call[]',
        },
        'identity': ['at', 'id'],
        'also': ['message'],
    },
    'episode': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'string',
            'datePublished': 'string',
            'content': 'string',
            'durationMs': 'integer',
            'episodeNumber': 'integer',
            'seasonNumber': 'integer',
            'guest': 'person[]',
            'series': 'podcast',
            'transcribe': 'transcript',
        },
        'identity': [],
        'also': [],
    },
    'event': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'string',
            'datePublished': 'string',
            'content': 'string',
            'allDay': 'boolean',
            'dateUpdated': 'datetime',
            'endDate': 'datetime',
            'eventType': 'string',
            'icalUid': 'string',
            'recurrence': 'string[]',
            'showAs': 'string',
            'sourceTitle': 'string',
            'sourceUrl': 'url',
            'startDate': 'datetime',
            'status': 'string',
            'timezone': 'string',
            'visibility': 'string',
            'at': 'actor',
            'attachments': 'file[]',
            'creator': 'person',
            'involves': 'person[]',
            'location': 'place',
            'organizer': 'person',
        },
        'identity': ['at', 'id'],
        'also': [],
    },
    'file': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'string',
            'datePublished': 'string',
            'content': 'string',
            'encoding': 'string',
            'filename': 'string',
            'format': 'string',
            'kind': 'string',
            'lineCount': 'integer',
            'mimeType': 'string',
            'path': 'string',
            'sha': 'string',
            'size': 'integer',
            'attachedTo': 'message',
            'repository': 'repository',
        },
        'identity': [],
        'also': [],
    },
    'folder': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'string',
            'datePublished': 'string',
            'content': 'string',
            'hasReadme': 'boolean',
            'path': 'string',
            'workspaceType': 'string',
            'contains': 'file[]',
            'repository': 'repository',
        },
        'identity': ['path'],
        'also': [],
    },
    'git_commit': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'account',
            'datePublished': 'string',
            'content': 'string',
            'additions': 'integer',
            'committedAt': 'datetime',
            'deletions': 'integer',
            'filesChanged': 'integer',
            'message': 'text',
            'sha': 'string',
            'shortHash': 'string',
            'committer': 'account',
            'parent': 'git_commit',
            'repository': 'repository',
        },
        'identity': [],
        'also': [],
    },
    'group': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'string',
            'datePublished': 'string',
            'content': 'string',
            'category': 'string',
            'memberCount': 'integer',
        },
        'identity': ['at', 'id'],
        'also': [],
    },
    'hardware': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'string',
            'datePublished': 'string',
            'content': 'string',
            'aisle': 'string',
            'availability': 'string',
            'barcode': 'string',
            'calories': 'number',
            'categories': 'string[]',
            'category': 'string',
            'currency': 'string',
            'department': 'string',
            'images': 'json',
            'modelNumber': 'string',
            'novaGroup': 'integer',
            'nutritionScore': 'string',
            'originalPrice': 'string',
            'originalPriceAmount': 'number',
            'price': 'string',
            'priceAmount': 'number',
            'quantity': 'integer',
            'serialNumber': 'string',
            'servingSize': 'string',
            'sku': 'string',
            'soldByWeight': 'boolean',
            'specs': 'json',
            'weight': 'string',
            'weightUnit': 'string',
            'weightValue': 'number',
            'brand': 'brand',
            'manufacturer': 'organization',
            'tagged': 'tag[]',
        },
        'identity': ['serialNumber'],
        'also': ['product'],
    },
    'image': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'string',
            'datePublished': 'string',
            'content': 'string',
            'altText': 'string',
            'appName': 'string',
            'displayId': 'integer',
            'displayIndex': 'integer',
            'encoding': 'string',
            'filename': 'string',
            'format': 'string',
            'height': 'integer',
            'kind': 'string',
            'lineCount': 'integer',
            'mimeType': 'string',
            'path': 'string',
            'sha': 'string',
            'size': 'integer',
            'width': 'integer',
            'windowId': 'integer',
            'attachedTo': 'message',
            'repository': 'repository',
        },
        'identity': [],
        'also': ['file'],
    },
    'invitation': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'string',
            'datePublished': 'string',
            'content': 'string',
            'acceptedAt': 'datetime',
            'email': 'string',
            'expiresAt': 'datetime',
            'invitationType': 'string',
            'message': 'text',
            'revokedAt': 'datetime',
            'role': 'string',
            'status': 'string',
            'token': 'string',
            'at': 'actor',
            'invitee': 'account',
            'inviter': 'account',
            'organization': 'organization',
        },
        'identity': ['at', 'id'],
        'also': [],
    },
    'job': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'string',
            'datePublished': 'string',
            'content': 'string',
            'boot_epoch': 'integer',
            'config': 'json',
            'kind': 'string',
            'status': 'string',
            'produced': 'conversation',
            'requested_by': 'account',
        },
        'identity': ['name', 'boot_epoch'],
        'also': [],
    },
    'leg': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'string',
            'datePublished': 'string',
            'content': 'string',
            'arrivalTime': 'datetime',
            'cabinClass': 'string',
            'carbonEmissions': 'json',
            'departureTime': 'datetime',
            'duration': 'string',
            'durationMinutes': 'integer',
            'flightNumber': 'string',
            'layoverMinutes': 'integer',
            'polyline': 'string',
            'sequence': 'integer',
            'trace': 'json',
            'tracePointCount': 'integer',
            'vehicleType': 'string',
            'aircraft': 'aircraft',
            'carrier': 'organization',
            'destination': 'place',
            'origin': 'place',
            'trip': 'trip',
        },
        'identity': [],
        'also': [],
    },
    'list': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'string',
            'datePublished': 'string',
            'content': 'string',
            'isDefault': 'boolean',
            'isPublic': 'boolean',
            'listId': 'string',
            'listType': 'string',
            'privacy': 'string',
            'at': 'actor',
            'belongsTo': 'account',
            'contains': 'product[]',
        },
        'identity': ['at', 'id'],
        'also': [],
    },
    'loaded_model': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'string',
            'datePublished': 'string',
            'content': 'string',
            'digest': 'string',
            'expiresAt': 'datetime',
            'quantization': 'string',
            'size': 'string',
            'sizeVram': 'integer',
            'vramUsage': 'string',
        },
        'identity': [],
        'also': [],
    },
    'mcp_session': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'string',
            'datePublished': 'string',
            'content': 'string',
            'client': 'string',
            'endedAt': 'datetime',
            'gitBranch': 'string',
            'messageCount': 'integer',
            'projectId': 'string',
            'sessionType': 'string',
            'startedAt': 'datetime',
            'tokenCount': 'integer',
            'folder': 'folder',
            'participant': 'actor',
        },
        'identity': ['client', 'projectId', 'gitBranch'],
        'also': [],
    },
    'meeting': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'string',
            'datePublished': 'string',
            'content': 'string',
            'allDay': 'boolean',
            'calendarLink': 'url',
            'conferenceProvider': 'string',
            'dateUpdated': 'datetime',
            'endDate': 'datetime',
            'eventType': 'string',
            'icalUid': 'string',
            'isVirtual': 'boolean',
            'meetingUrl': 'url',
            'phoneDialIn': 'string',
            'recurrence': 'string[]',
            'showAs': 'string',
            'sourceTitle': 'string',
            'sourceUrl': 'url',
            'startDate': 'datetime',
            'status': 'string',
            'timezone': 'string',
            'visibility': 'string',
            'at': 'actor',
            'attachments': 'file[]',
            'creator': 'person',
            'involves': 'person[]',
            'location': 'place',
            'organizer': 'person',
            'transcribe': 'transcript',
        },
        'identity': [],
        'also': ['event'],
    },
    'memex': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'string',
            'datePublished': 'string',
            'content': 'string',
            'description': 'text',
            'edgeCount': 'integer',
            'filePath': 'string',
            'fileSize': 'string',
            'nodeCount': 'integer',
            'origin': 'string',
            'published': 'boolean',
            'snapshotOf': 'datetime',
            'forkedFrom': 'memex',
            'owner': 'person',
            'snapshots': 'memex[]',
        },
        'identity': [],
        'also': [],
    },
    'message': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'string',
            'datePublished': 'string',
            'content': 'string',
            'isOutgoing': 'boolean',
            'isStarred': 'boolean',
            'at': 'actor',
            'from': 'actor',
            'inConversation': 'conversation',
            'repliesTo': 'message',
            'toolCalls': 'tool_call[]',
        },
        'identity': ['at', 'id'],
        'also': [],
    },
    'model': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'string',
            'datePublished': 'string',
            'content': 'string',
            'contextLength': 'integer',
            'contextWindow': 'integer',
            'digest': 'string',
            'family': 'string',
            'format': 'string',
            'maxOutput': 'integer',
            'modality': 'string[]',
            'modelType': 'string',
            'parameterSize': 'string',
            'pricingInput': 'string',
            'pricingOutput': 'string',
            'quantization': 'string',
            'quantizationLevel': 'string',
            'size': 'string',
            'at': 'actor',
        },
        'identity': ['at', 'name'],
        'also': [],
    },
    'note': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'string',
            'datePublished': 'string',
            'content': 'string',
            'isPinned': 'boolean',
            'noteType': 'string',
            'createdBy': 'person',
            'extractedFrom': 'webpage',
            'references': 'note[]',
        },
        'identity': [],
        'also': [],
    },
    'offer': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'string',
            'datePublished': 'string',
            'content': 'string',
            'availability': 'string',
            'bookingToken': 'string',
            'currency': 'string',
            'offerType': 'string',
            'price': 'number',
            'validFrom': 'datetime',
            'validUntil': 'datetime',
            'for': 'product',
            'offeredBy': 'organization',
            'trips': 'trip[]',
        },
        'identity': [],
        'also': [],
    },
    'order': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'string',
            'datePublished': 'string',
            'content': 'string',
            'currency': 'string',
            'deliveryDate': 'datetime',
            'deliveryFee': 'number',
            'eta': 'string',
            'fareBreakdown': 'json',
            'orderDate': 'datetime',
            'orderId': 'string',
            'originalTotal': 'string',
            'originalTotalAmount': 'number',
            'savings': 'number',
            'status': 'string',
            'subtotal': 'number',
            'summary': 'string',
            'taxes': 'number',
            'tipAmount': 'number',
            'total': 'string',
            'totalAmount': 'number',
            'at': 'actor',
            'contains': 'product[]',
            'delivery': 'trip',
            'shippingAddress': 'place',
            'store': 'place',
            'tracking': 'webpage',
        },
        'identity': ['at', 'orderId'],
        'also': [],
    },
    'organization': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'string',
            'datePublished': 'string',
            'content': 'string',
            'actorType': 'string',
            'founded': 'datetime',
            'industry': 'string',
            'domain': 'domain',
            'headquarters': 'place',
            'member': 'person[]',
            'website': 'website',
        },
        'identity': ['url'],
        'also': ['actor'],
    },
    'person': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'string',
            'datePublished': 'string',
            'content': 'string',
            'about': 'text',
            'actorType': 'string',
            'birthday': 'datetime',
            'firstName': 'string',
            'gender': 'string',
            'joinedDate': 'datetime',
            'lastActive': 'datetime',
            'lastName': 'string',
            'middleName': 'string',
            'nickname': 'string',
            'notes': 'text',
            'accounts': 'account[]',
            'location': 'place',
            'roles': 'role[]',
            'website': 'website',
        },
        'identity': [],
        'also': ['actor'],
    },
    'place': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'string',
            'datePublished': 'string',
            'content': 'string',
            'accuracy': 'string',
            'businessStatus': 'string',
            'categories': 'string[]',
            'city': 'string',
            'country': 'string',
            'countryCode': 'string',
            'district': 'string',
            'featureType': 'string',
            'fullAddress': 'string',
            'googlePlaceId': 'string',
            'hours': 'json',
            'latitude': 'number',
            'locality': 'string',
            'longitude': 'number',
            'mapboxId': 'string',
            'neighborhood': 'string',
            'phone': 'string',
            'placeFormatted': 'string',
            'postalCode': 'string',
            'priceLevel': 'string',
            'rating': 'number',
            'region': 'string',
            'reviewCount': 'integer',
            'street': 'string',
            'streetNumber': 'string',
            'timezone': 'string',
            'website': 'url',
            'wikidataId': 'string',
            'brand': 'organization',
            'offers': 'product[]',
        },
        'identity': ['googlePlaceId', 'mapboxId'],
        'also': [],
    },
    'playlist': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'string',
            'datePublished': 'string',
            'content': 'string',
            'isDefault': 'boolean',
            'isPublic': 'boolean',
            'listId': 'string',
            'listType': 'string',
            'privacy': 'string',
            'at': 'actor',
            'belongsTo': 'account',
            'contains': 'video[]',
        },
        'identity': [],
        'also': ['list'],
    },
    'podcast': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'string',
            'datePublished': 'string',
            'content': 'string',
            'feedUrl': 'url',
            'at': 'actor',
            'episode': 'episode[]',
            'host': 'person[]',
        },
        'identity': ['at', 'id'],
        'also': [],
    },
    'post': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'string',
            'datePublished': 'string',
            'content': 'string',
            'externalUrl': 'url',
            'postType': 'string',
            'attachment': 'file[]',
            'contains': 'video[]',
            'media': 'image[]',
            'postedBy': 'account',
            'publish': 'community',
            'replies': 'post[]',
            'repliesTo': 'post',
        },
        'identity': ['at', 'id'],
        'also': [],
    },
    'product': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'string',
            'datePublished': 'string',
            'content': 'string',
            'aisle': 'string',
            'availability': 'string',
            'barcode': 'string',
            'calories': 'number',
            'categories': 'string[]',
            'category': 'string',
            'currency': 'string',
            'department': 'string',
            'images': 'json',
            'novaGroup': 'integer',
            'nutritionScore': 'string',
            'originalPrice': 'string',
            'originalPriceAmount': 'number',
            'price': 'string',
            'priceAmount': 'number',
            'quantity': 'integer',
            'servingSize': 'string',
            'sku': 'string',
            'soldByWeight': 'boolean',
            'weight': 'string',
            'weightUnit': 'string',
            'weightValue': 'number',
            'brand': 'brand',
            'manufacturer': 'organization',
            'tagged': 'tag[]',
        },
        'identity': [],
        'also': [],
    },
    'project': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'string',
            'datePublished': 'string',
            'content': 'string',
            'color': 'string',
            'state': 'string',
        },
        'identity': ['at', 'id'],
        'also': [],
    },
    'protocol': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'string',
            'datePublished': 'string',
            'content': 'string',
            'homepage': 'url',
            'rfc': 'string',
            'wikidataId': 'string',
        },
        'identity': ['name'],
        'also': [],
    },
    'quote': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'string',
            'datePublished': 'string',
            'content': 'string',
            'context': 'string',
            'year': 'integer',
        },
        'identity': [],
        'also': [],
    },
    'repository': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'string',
            'datePublished': 'string',
            'content': 'string',
            'defaultBranch': 'string',
            'forks': 'integer',
            'isArchived': 'boolean',
            'isPrivate': 'boolean',
            'language': 'string',
            'license': 'string',
            'openIssues': 'integer',
            'size': 'integer',
            'stars': 'integer',
            'topics': 'string[]',
            'forkedFrom': 'repository',
            'owner': 'account',
        },
        'identity': ['path', 'url'],
        'also': [],
    },
    'result': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'string',
            'datePublished': 'string',
            'content': 'string',
            'indexedAt': 'datetime',
            'resultType': 'string',
        },
        'identity': [],
        'also': [],
    },
    'review': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'string',
            'datePublished': 'string',
            'content': 'string',
            'externalUrl': 'url',
            'isVerified': 'boolean',
            'postType': 'string',
            'rating': 'number',
            'ratingMax': 'number',
            'tags': 'string[]',
            'attachment': 'file[]',
            'contains': 'video[]',
            'media': 'image[]',
            'postedBy': 'account',
            'publish': 'community',
            'replies': 'post[]',
            'repliesTo': 'post',
            'reviews': 'product',
        },
        'identity': [],
        'also': ['post'],
    },
    'role': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'string',
            'datePublished': 'string',
            'content': 'string',
            'department': 'string',
            'endDate': 'datetime',
            'roleType': 'string',
            'startDate': 'datetime',
            'title': 'string',
            'organization': 'organization',
            'person': 'person',
        },
        'identity': [],
        'also': [],
    },
    'search': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'string',
            'datePublished': 'string',
            'content': 'string',
            'query': 'string',
            'resultCount': 'integer',
            'searchCount': 'integer',
            'searchedAt': 'datetime',
        },
        'identity': ['query'],
        'also': [],
    },
    'shelf': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'string',
            'datePublished': 'string',
            'content': 'string',
            'isDefault': 'boolean',
            'isExclusive': 'boolean',
            'isPublic': 'boolean',
            'listId': 'string',
            'listType': 'string',
            'privacy': 'string',
            'at': 'actor',
            'belongsTo': 'account',
            'contains': 'book[]',
        },
        'identity': [],
        'also': ['list'],
    },
    'shortcut': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'string',
            'datePublished': 'string',
            'content': 'string',
            'builtin': 'boolean',
            'filter': 'string',
            'target': 'string',
            'skill': 'skill',
        },
        'identity': ['name'],
        'also': [],
    },
    'simulation': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'string',
            'datePublished': 'string',
            'content': 'string',
            'actionCount': 'integer',
            'endedAt': 'datetime',
            'graphMode': 'string',
            'profile': 'string',
            'startedAt': 'datetime',
            'status': 'string',
            'task': 'text',
            'writeCount': 'integer',
            'agent': 'agent',
            'forkedFrom': 'simulation',
            'mountedMemex': 'memex[]',
            'primaryMemex': 'memex',
            'startedBy': 'person',
            'tether': 'hardware',
        },
        'identity': [],
        'also': [],
    },
    'skill': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'string',
            'datePublished': 'string',
            'content': 'string',
            'color': 'string',
            'description': 'text',
            'error': 'text',
            'skillId': 'string',
            'status': 'string',
            'privacyPolicy': 'webpage',
            'termsOfService': 'webpage',
            'website': 'website',
        },
        'identity': [],
        'also': [],
    },
    'software': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'string',
            'datePublished': 'string',
            'content': 'string',
            'aisle': 'string',
            'availability': 'string',
            'barcode': 'string',
            'calories': 'number',
            'categories': 'string[]',
            'category': 'string',
            'currency': 'string',
            'department': 'string',
            'images': 'json',
            'license': 'string',
            'novaGroup': 'integer',
            'nutritionScore': 'string',
            'openSource': 'boolean',
            'originalPrice': 'string',
            'originalPriceAmount': 'number',
            'platform': 'string[]',
            'price': 'string',
            'priceAmount': 'number',
            'quantity': 'integer',
            'repositoryUrl': 'url',
            'servingSize': 'string',
            'sku': 'string',
            'soldByWeight': 'boolean',
            'version': 'string',
            'weight': 'string',
            'weightUnit': 'string',
            'weightValue': 'number',
            'brand': 'brand',
            'developer': 'organization',
            'manufacturer': 'organization',
            'repository': 'repository',
            'tagged': 'tag[]',
        },
        'identity': ['url'],
        'also': ['product'],
    },
    'source': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'string',
            'datePublished': 'string',
            'content': 'string',
            'address': 'string',
            'description': 'text',
            'enabled': 'boolean',
            'lastSynced': 'datetime',
            'scanner': 'string',
            'sourceId': 'string',
            'folder': 'folder',
        },
        'identity': ['address'],
        'also': [],
    },
    'spec': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'string',
            'datePublished': 'string',
            'content': 'string',
            'encoding': 'string',
            'filename': 'string',
            'format': 'string',
            'kind': 'string',
            'labels': 'string[]',
            'lineCount': 'integer',
            'mimeType': 'string',
            'path': 'string',
            'priority': 'integer',
            'problem': 'text',
            'remoteId': 'string',
            'sha': 'string',
            'size': 'integer',
            'startedAt': 'datetime',
            'state': 'string',
            'successCriteria': 'text',
            'targetDate': 'datetime',
            'assignedTo': 'person',
            'attachedTo': 'message',
            'blockedBy': 'task[]',
            'blocks': 'task[]',
            'children': 'task[]',
            'dependsOn': 'spec[]',
            'parent': 'task',
            'project': 'project',
            'repository': 'repository',
            'supersedes': 'spec[]',
        },
        'identity': [],
        'also': ['task', 'file'],
    },
    'tag': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'string',
            'datePublished': 'string',
            'content': 'string',
            'color': 'string',
            'tagType': 'string',
        },
        'identity': [],
        'also': [],
    },
    'task': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'string',
            'datePublished': 'string',
            'content': 'string',
            'labels': 'string[]',
            'priority': 'integer',
            'remoteId': 'string',
            'startedAt': 'datetime',
            'state': 'string',
            'targetDate': 'datetime',
            'assignedTo': 'person',
            'blockedBy': 'task[]',
            'blocks': 'task[]',
            'children': 'task[]',
            'parent': 'task',
            'project': 'project',
            'repository': 'repository',
        },
        'identity': ['at', 'id'],
        'also': [],
    },
    'theme': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'string',
            'datePublished': 'string',
            'content': 'string',
            'colorScheme': 'string',
            'description': 'text',
            'family': 'string',
            'themeId': 'string',
            'wallpaper': 'image',
        },
        'identity': ['themeId'],
        'also': [],
    },
    'tool_call': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'string',
            'datePublished': 'string',
            'content': 'string',
            'durationMs': 'integer',
            'input': 'text',
            'isError': 'boolean',
            'output': 'text',
            'from': 'actor',
            'inMessage': 'message',
            'platform': 'product',
            'repliesTo': 'tool_call',
        },
        'identity': ['platform', 'id'],
        'also': [],
    },
    'transaction': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'string',
            'datePublished': 'string',
            'content': 'string',
            'amount': 'number',
            'balance': 'number',
            'category': 'string',
            'currency': 'string',
            'details': 'json',
            'notes': 'string',
            'pending': 'boolean',
            'postingDate': 'datetime',
            'recurring': 'boolean',
            'type': 'string',
            'account': 'account',
        },
        'identity': ['at', 'id'],
        'also': [],
    },
    'transcript': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'string',
            'datePublished': 'string',
            'content': 'string',
            'contentRole': 'string',
            'durationMs': 'integer',
            'language': 'string',
            'segmentCount': 'integer',
            'segments': 'json',
            'sourceType': 'string',
        },
        'identity': [],
        'also': [],
    },
    'trip': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'string',
            'datePublished': 'string',
            'content': 'string',
            'arrivalTime': 'datetime',
            'bookingToken': 'string',
            'cabinClass': 'string',
            'carbonEmissions': 'json',
            'currency': 'string',
            'departureTime': 'datetime',
            'distance': 'string',
            'duration': 'string',
            'durationMinutes': 'integer',
            'fare': 'string',
            'fareAmount': 'number',
            'isScheduled': 'boolean',
            'isSurge': 'boolean',
            'rating': 'string',
            'status': 'string',
            'stops': 'integer',
            'trackingUrl': 'url',
            'tripType': 'string',
            'vehicleType': 'string',
            'carrier': 'organization',
            'destination': 'place',
            'driver': 'person',
            'legs': 'leg[]',
            'order': 'order',
            'origin': 'place',
        },
        'identity': ['at', 'id'],
        'also': [],
    },
    'video': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'string',
            'datePublished': 'string',
            'content': 'string',
            'codec': 'string',
            'durationMs': 'integer',
            'encoding': 'string',
            'filename': 'string',
            'format': 'string',
            'frameRate': 'number',
            'kind': 'string',
            'lineCount': 'integer',
            'mimeType': 'string',
            'path': 'string',
            'resolution': 'string',
            'sha': 'string',
            'size': 'integer',
            'addTo': 'playlist',
            'attachedTo': 'message',
            'channel': 'channel',
            'repository': 'repository',
            'transcribe': 'transcript',
        },
        'identity': [],
        'also': ['file'],
    },
    'volume': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'string',
            'datePublished': 'string',
            'content': 'string',
            'filesystem': 'string',
            'freeBytes': 'integer',
            'path': 'string',
            'readOnly': 'boolean',
            'removable': 'boolean',
            'totalBytes': 'integer',
            'usedBytes': 'integer',
            'volumeType': 'string',
            'contains': 'folder[]',
        },
        'identity': [],
        'also': [],
    },
    'webpage': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'string',
            'datePublished': 'string',
            'content': 'string',
            'contentType': 'string',
            'error': 'string',
            'lastVisitUnix': 'integer',
            'visitCount': 'integer',
        },
        'identity': ['url'],
        'also': [],
    },
    'website': {
        'fields': {
            'id': 'string',
            'name': 'string',
            'text': 'string',
            'url': 'string',
            'image': 'string',
            'author': 'string',
            'datePublished': 'string',
            'content': 'string',
            'anonymous': 'boolean',
            'claimToken': 'string',
            'claimUrl': 'url',
            'expiresAt': 'datetime',
            'status': 'string',
            'versionId': 'string',
            'domain': 'domain',
            'ownedBy': 'organization',
        },
        'identity': ['url'],
        'also': [],
    },
}
