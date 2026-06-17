"""Auto-generated TypedDict classes from shape YAML — do not edit.

Generated from 116 shapes.
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
    display: str
    displayName: str
    email: str
    handle: str
    identifier: str
    isActive: bool
    issuer: str
    joinedDate: str
    lastActive: str
    lastProfileFetch: str
    metadata: Any
    phone: str
    userId: str


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
    allDay: bool
    changedKeys: list[str]
    currentUrl: str
    dateUpdated: str
    distinctId: str
    duration: float
    endDate: str
    icalUid: str
    properties: Any
    recurrence: list[str]
    showAs: str
    sourceTitle: str
    sourceUrl: str
    startDate: str
    status: str
    success: bool
    timezone: str
    toolName: str
    visibility: str


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
    customizationGroups: Any
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


class Airline(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    actorType: str
    alliance: str
    callsign: str
    country: str
    iataCode: str
    icaoCode: str
    industry: str


class Airport(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    city: str
    country: str
    countryCode: str
    elevationFt: int
    iataCode: str
    icaoCode: str
    terminalCount: int
    timezone: str


class App(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    account: Any
    color: str
    composition: Any
    defaultRoute: str
    defaultView: str
    description: str
    error: str
    handles: list[str]
    iconRole: str
    isSystem: bool
    route: str
    status: str


class AuthChallenge(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    artifact: str
    continueWith: str
    expiresAt: str
    instructions: str
    kind: str
    payload: str
    retrieval: Any


class Birth(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    additionalName: str
    allDay: bool
    currentUrl: str
    dateUpdated: str
    distinctId: str
    endDate: str
    familyName: str
    gender: str
    givenName: str
    honorificPrefix: str
    honorificSuffix: str
    icalUid: str
    legalName: str
    maidenName: str
    nameOrder: str
    nickname: str
    phoneticFamilyName: str
    phoneticGivenName: str
    properties: Any
    recurrence: list[str]
    showAs: str
    sortAs: str
    sourceTitle: str
    sourceUrl: str
    startDate: str
    status: str
    timezone: str
    visibility: str


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
    copyrightYear: int
    coverage: str
    currency: str
    customizationGroups: Any
    dateCreated: Any
    department: str
    description: str
    format: str
    genres: list[str]
    images: Any
    isbn: str
    isbn13: str
    language: str
    license: str
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
    tags: list[str]
    weight: str
    weightUnit: str
    weightValue: float


class BookingOffer(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    allDay: bool
    approvedAt: str
    baseAmount: float
    blob: str
    cartId: str
    checkoutUrl: str
    conditions: Any
    confirmEndpoint: str
    contactEmail: str
    contactPhone: str
    currency: str
    currentUrl: str
    dateUpdated: str
    distinctId: str
    endDate: str
    expiresAt: str
    feesAmount: float
    hasVoidWindow: bool
    icalUid: str
    isChangeable: bool
    isRefundable: bool
    itineraryHash: str
    preparedAt: str
    presentedAt: str
    properties: Any
    recurrence: list[str]
    referenceNumber: str
    review: str
    showAs: str
    signature: str
    signatureAlg: str
    signedBy: str
    sourceTitle: str
    sourceUrl: str
    startDate: str
    status: str
    taxAmount: float
    timezone: str
    totalAmount: float
    visibility: str
    voidWindowEndsAt: str


class Bookmark(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    address: str
    handle: str


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
    primaryColor: str
    tagline: str
    textColor: str


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
    subscriberCount: int


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
    currentUrl: str
    dateUpdated: str
    distinctId: str
    endDate: str
    icalUid: str
    isFull: bool
    properties: Any
    recurrence: list[str]
    showAs: str
    sourceTitle: str
    sourceUrl: str
    spotsRemaining: int
    startDate: str
    status: str
    timezone: str
    visibility: str


class Community(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    allowCrypto: bool
    memberCount: int
    privacy: str
    subscriberCount: int


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
    historyId: str
    isArchived: bool
    isGroup: bool
    messageCount: int
    source: str
    unreadCount: int


class Conversion(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    allDay: bool
    currentUrl: str
    dateUpdated: str
    distinctId: str
    endDate: str
    factor: float
    icalUid: str
    kind: str
    properties: Any
    rate: float
    recurrence: list[str]
    showAs: str
    sourceTitle: str
    sourceUrl: str
    startDate: str
    status: str
    timezone: str
    visibility: str


class CreativeWork(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    copyrightYear: int
    coverage: str
    dateCreated: Any
    description: str
    language: str
    license: str
    tags: list[str]


class Credential(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    domain: str
    identifier: str
    itemType: str
    lastVerified: str
    obtainedAt: str
    refreshable: bool
    source: str
    storeRowId: int


class Cursor(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    copyrightYear: int
    coverage: str
    dateCreated: Any
    description: str
    dimension: int
    encoding: str
    filename: str
    format: str
    hotspotX: int
    hotspotY: int
    kind: str
    language: str
    license: str
    lineCount: int
    mimeType: str
    path: str
    purpose: str
    sha: str
    size: int
    tags: list[str]


class Dimension(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    amount: int
    current: int
    dimensionless: bool
    key: str
    label: str
    length: int
    luminous: int
    mass: int
    temperature: int
    time: int


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
    priority: int
    recordId: str
    recordName: str
    recordType: str
    ttl: int
    type: str
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
    ccRaw: str
    conversationId: str
    deliveredTo: str
    draftId: str
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
    currentUrl: str
    dateUpdated: str
    distinctId: str
    endDate: str
    icalUid: str
    properties: Any
    recurrence: list[str]
    showAs: str
    sourceTitle: str
    sourceUrl: str
    startDate: str
    status: str
    timezone: str
    visibility: str


class Fare(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    basePrice: float
    bookingCode: str
    changeable: bool
    class_: str  # class
    components: int
    conditions: Any
    currency: str
    fareFamily: str
    identifier: str
    milesEarned: int
    passengerType: str
    pointsEarned: int
    productType: str
    refundable: bool
    restrictions: list[str]


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


class FinancialAccount(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    accountId: str
    accountNumber: str
    accountType: str
    available: float
    balance: float
    cardType: str
    creditLimit: float
    currency: str
    identifier: str
    interestRate: float
    last4: str
    minimumPayment: float
    routingNumber: str


class Flight(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    allDay: bool
    arrivalTime: str
    cabinClass: str
    carbonEmissions: Any
    currentUrl: str
    dateUpdated: str
    departureTime: str
    distinctId: str
    duration: str
    durationMinutes: int
    endDate: str
    flightNumber: str
    icalUid: str
    layoverMinutes: int
    polyline: str
    properties: Any
    recurrence: list[str]
    sequence: int
    showAs: str
    sourceTitle: str
    sourceUrl: str
    startDate: str
    status: str
    stops: int
    timezone: str
    trace: Any
    tracePointCount: int
    vehicleType: str
    visibility: str


class Font(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    copyrightYear: int
    coverage: str
    dateCreated: Any
    description: str
    designerUrl: str
    family: str
    formats: list[str]
    genericFamily: str
    glyphCount: int
    language: str
    license: str
    licenseInfoUrl: str
    postscriptName: str
    scripts: list[str]
    styles: list[str]
    tags: list[str]
    vendorUrl: str
    weights: list[int]


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
    allDay: bool
    committedAt: str
    currentUrl: str
    dateUpdated: str
    deletions: int
    distinctId: str
    endDate: str
    filesChanged: int
    icalUid: str
    message: str
    properties: Any
    recurrence: list[str]
    sha: str
    shortHash: str
    showAs: str
    sourceTitle: str
    sourceUrl: str
    startDate: str
    status: str
    timezone: str
    visibility: str


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


class HealthBiomarker(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    analyteType: str
    category: str
    description: str
    loincCode: str
    measure: str


class HealthCondition(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    allDay: bool
    bodySite: str
    clinicalArea: str
    clinicalStatus: str
    currentUrl: str
    dateUpdated: str
    distinctId: str
    endDate: str
    icalUid: str
    icd10Code: str
    mitigation: str
    properties: Any
    proximity: str
    recurrence: list[str]
    severity: str
    showAs: str
    snomedCode: str
    sourceTitle: str
    sourceUrl: str
    startDate: str
    status: str
    timezone: str
    verificationStatus: str
    visibility: str


class HealthImmunization(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    allDay: bool
    currentUrl: str
    cvxCode: str
    dateAdministered: str
    dateUpdated: str
    diseaseTarget: str
    distinctId: str
    doseNumber: int
    endDate: str
    icalUid: str
    lotNumber: str
    manufacturer: str
    notes: str
    properties: Any
    recurrence: list[str]
    route: str
    seriesDoses: int
    showAs: str
    site: str
    sourceTitle: str
    sourceUrl: str
    startDate: str
    status: str
    timezone: str
    visibility: str


class HealthLab(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    accreditation: str
    actorType: str
    ccn: str
    cliaNumber: str
    industry: str
    labType: str
    npi: str


class HealthPanel(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    allDay: bool
    arrangement: str
    currentUrl: str
    dateUpdated: str
    default_view: str
    description: str
    distinctId: str
    endDate: str
    fasting: bool
    icalUid: str
    icon_size: int
    isDefault: bool
    isPublic: bool
    itemCount: int
    listId: str
    listType: str
    member_shape: str
    ordering_mode: str
    panelCode: str
    path: str
    privacy: str
    properties: Any
    recurrence: list[str]
    showAs: str
    sort_by: str
    sourceTitle: str
    sourceUrl: str
    startDate: str
    status: str
    timezone: str
    visibility: str


class HealthProcedure(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    allDay: bool
    bodySite: str
    cptCode: str
    currentUrl: str
    dateUpdated: str
    distinctId: str
    endDate: str
    findings: str
    followUp: str
    icalUid: str
    outcome: str
    performedDate: str
    procedureType: str
    properties: Any
    recurrence: list[str]
    showAs: str
    snomedCode: str
    sourceTitle: str
    sourceUrl: str
    startDate: str
    status: str
    timezone: str
    visibility: str


class HealthReferenceRange(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    ageHigh: float
    ageLow: float
    allDay: bool
    category: str
    currentUrl: str
    dateUpdated: str
    distinctId: str
    endDate: str
    fasting: bool
    gestationalAge: str
    high: float
    icalUid: str
    low: float
    method: str
    pregnancy: str
    properties: Any
    provenance: str
    recurrence: list[str]
    refText: str
    sex: str
    showAs: str
    sourceTitle: str
    sourceUrl: str
    startDate: str
    status: str
    timeOfDay: str
    timezone: str
    unit: str
    visibility: str


class Icon(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    component: str
    copyrightYear: int
    coverage: str
    dateCreated: Any
    description: str
    dimension: int
    format: str
    language: str
    license: str
    purpose: str
    style: str
    tags: list[str]


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
    copyrightYear: int
    coverage: str
    dateCreated: Any
    description: str
    displayId: int
    displayIndex: int
    encoding: str
    filename: str
    format: str
    height: int
    kind: str
    language: str
    license: str
    lineCount: int
    mimeType: str
    path: str
    sha: str
    size: int
    tags: list[str]
    width: int
    windowId: int


class InsuranceCoverage(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    coinsurance: float
    copay: float
    currency: str
    deductible: float
    limit: float
    limitBasis: str
    notes: str
    outOfPocketMax: float
    requiresPreauth: bool
    requiresReferral: bool
    waitingPeriodMonths: float


class InsurancePolicy(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    allDay: bool
    autoRenew: bool
    billingType: str
    coverageType: str
    currency: str
    currentUrl: str
    dateUpdated: str
    distinctId: str
    endDate: str
    groupNumber: str
    guestPassQuantity: int
    icalUid: str
    memberId: str
    network: str
    policyNumber: str
    price: float
    properties: Any
    recurrence: list[str]
    showAs: str
    sourceTitle: str
    sourceUrl: str
    startDate: str
    status: str
    tier: str
    timezone: str
    useCount: int
    visibility: str


class IntellectualProperty(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    category: str
    filingBasis: str
    identifier: str
    mark: str
    niceClass: list[int]
    register: str
    renewalPeriod: str
    status: str
    validIn: str
    verificationUrl: str


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
    allDay: bool
    currentUrl: str
    dateUpdated: str
    distinctId: str
    email: str
    endDate: str
    icalUid: str
    invitationType: str
    message: str
    properties: Any
    recurrence: list[str]
    revokedAt: str
    role: str
    showAs: str
    sourceTitle: str
    sourceUrl: str
    startDate: str
    status: str
    timezone: str
    token: str
    visibility: str


class Issue(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    commentCount: int
    community: str
    declined: bool
    externalUrl: str
    postType: str
    score: int


class Launch(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    allDay: bool
    articleUrl: str
    crewIds: list[str]
    currentUrl: str
    dateUpdated: str
    distinctId: str
    endDate: str
    flightNumber: int
    icalUid: str
    landingOutcomes: Any
    launchpadId: str
    patchImage: str
    properties: Any
    recurrence: list[str]
    reusedBoosters: list[str]
    rocketId: str
    showAs: str
    sourceTitle: str
    sourceUrl: str
    startDate: str
    status: str
    timezone: str
    visibility: str
    webcastUrl: str
    wikipediaUrl: str


class Leg(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    allDay: bool
    arrivalTime: str
    cabinClass: str
    carbonEmissions: Any
    currentUrl: str
    dateUpdated: str
    departureTime: str
    distinctId: str
    duration: str
    durationMinutes: int
    endDate: str
    flightNumber: str
    icalUid: str
    layoverMinutes: int
    polyline: str
    properties: Any
    recurrence: list[str]
    sequence: int
    showAs: str
    sourceTitle: str
    sourceUrl: str
    startDate: str
    status: str
    timezone: str
    trace: Any
    tracePointCount: int
    vehicleType: str
    visibility: str


class List(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    arrangement: str
    default_view: str
    icon_size: int
    isDefault: bool
    isPublic: bool
    itemCount: int
    listId: str
    listType: str
    member_shape: str
    ordering_mode: str
    path: str
    privacy: str
    sort_by: str


class LoadedModel(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    allDay: bool
    currentUrl: str
    dateUpdated: str
    digest: str
    distinctId: str
    endDate: str
    icalUid: str
    properties: Any
    quantization: str
    recurrence: list[str]
    showAs: str
    size: str
    sizeVram: int
    sourceTitle: str
    sourceUrl: str
    startDate: str
    status: str
    timezone: str
    visibility: str
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


class Measure(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    allDay: bool
    currentUrl: str
    dateUpdated: str
    distinctId: str
    endDate: str
    flag: str
    icalUid: str
    notes: str
    properties: Any
    recurrence: list[str]
    refHigh: float
    refLow: float
    refText: str
    showAs: str
    sourceTitle: str
    sourceUrl: str
    startDate: str
    status: str
    timezone: str
    value: float
    valueText: str
    visibility: str


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
    currentUrl: str
    dateUpdated: str
    distinctId: str
    endDate: str
    icalUid: str
    isVirtual: bool
    meetingType: str
    meetingUrl: str
    phoneDialIn: str
    properties: Any
    recurrence: list[str]
    showAs: str
    sourceTitle: str
    sourceUrl: str
    startDate: str
    status: str
    timezone: str
    visibility: str


class Membership(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    allDay: bool
    autoRenew: bool
    billingType: str
    currency: str
    currentUrl: str
    dateUpdated: str
    distinctId: str
    endDate: str
    guestPassQuantity: int
    icalUid: str
    price: float
    properties: Any
    recurrence: list[str]
    showAs: str
    sourceTitle: str
    sourceUrl: str
    startDate: str
    status: str
    tier: str
    timezone: str
    useCount: int
    visibility: str


class Message(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    conversationId: str
    isOutgoing: bool
    isStarred: bool


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


class Module(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    path: str
    planned: bool
    role: str
    status: str
    version: str


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


class Offer(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    allDay: bool
    availability: str
    bookingToken: str
    currency: str
    currentUrl: str
    dateUpdated: str
    departureToken: str
    distinctId: str
    endDate: str
    icalUid: str
    offerType: str
    price: float
    properties: Any
    recurrence: list[str]
    showAs: str
    sourceTitle: str
    sourceUrl: str
    startDate: str
    status: str
    timezone: str
    visibility: str


class Order(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    allDay: bool
    body: str
    currency: str
    currentUrl: str
    dateUpdated: str
    deliveryDate: str
    deliveryFee: float
    deliveryInstructions: str
    distinctId: str
    endDate: str
    eta: str
    fareBreakdown: Any
    head: str
    icalUid: str
    interactionType: str
    itemStates: Any
    latestArrival: str
    messages: Any
    orderDate: str
    orderId: str
    orderUuid: str
    originalTotal: str
    originalTotalAmount: float
    progress: float
    progressTotal: float
    properties: Any
    recurrence: list[str]
    savings: float
    showAs: str
    sourceTitle: str
    sourceUrl: str
    startDate: str
    status: str
    subtotal: float
    summary: str
    taxes: float
    timeline: Any
    timezone: str
    tipAmount: float
    total: str
    totalAmount: float
    visibility: str


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
    industry: str


class Outcome(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    archived: bool
    baseline: str
    current: str
    metric: str
    priority: int
    statement: str
    status: str
    target: str


class Pass(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    allDay: bool
    boardingGroup: str
    checkinStatus: str
    currency: str
    currentUrl: str
    dateUpdated: str
    distinctId: str
    endDate: str
    gate: str
    icalUid: str
    isAllDayPass: bool
    nameOnTicket: str
    price: float
    properties: Any
    purchasedQuantity: int
    quantity: int
    recurrence: list[str]
    seatAssignment: str
    showAs: str
    sourceTitle: str
    sourceUrl: str
    startDate: str
    status: str
    terminal: str
    ticketClass: str
    ticketNumber: str
    timezone: str
    useCount: int
    visibility: str


class PaymentMethod(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    balance: float
    binRange: str
    brand: str
    currency: str
    customDescription: str
    displayName: str
    expMonth: int
    expYear: int
    expirationDate: str
    fingerprint: str
    holderName: str
    identifier: str
    isDefault: bool
    isExpired: bool
    isPrimary: bool
    isSelected: bool
    last4: str
    metadata: Any
    providerTokens: Any
    status: str
    subtype: str
    type: str


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
    notes: str


class Persona(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    goals: list[str]
    headline: str
    painPoints: list[str]
    quote: str
    reachesFor: str
    who: str


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
    closedMessage: str
    country: str
    countryCode: str
    district: str
    eta: str
    featureType: str
    fullAddress: str
    googlePlaceId: str
    hours: Any
    isOrderable: bool
    latitude: float
    locality: str
    longitude: float
    mapboxId: str
    neighborhood: str
    phone: str
    placeFormatted: str
    postalCode: str
    priceLevel: str
    productCount: int
    rating: float
    region: str
    reviewCount: int
    street: str
    streetNumber: str
    timezone: str
    website: str
    wikidataId: str


class Playlist(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    arrangement: str
    default_view: str
    icon_size: int
    isDefault: bool
    isPublic: bool
    itemCount: int
    listId: str
    listType: str
    member_shape: str
    ordering_mode: str
    path: str
    privacy: str
    sort_by: str


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


class Post(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    commentCount: int
    community: str
    externalUrl: str
    postType: str
    score: int


class Practice(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    aliases: list[str]
    code: str
    codeSystem: str
    description: str


class Principle(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    domain: str
    rationale: str
    statement: str
    status: str


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
    customizationGroups: Any
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
    parentId: str
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


class Qualification(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    category: str
    identifier: str
    level: str
    renewalPeriod: str
    status: str
    validIn: str
    verificationUrl: str


class QuantityKind(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    key: str
    label: str


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


class Reservation(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    allDay: bool
    availableActions: list[str]
    baseAmount: float
    bookingTime: str
    bookingType: str
    checkinUrl: str
    conditions: Any
    currency: str
    currentUrl: str
    dateUpdated: str
    distinctId: str
    endDate: str
    endTime: str
    icalUid: str
    modifiedTime: str
    partySize: int
    properties: Any
    recurrence: list[str]
    reservationId: str
    reservationType: str
    showAs: str
    sourceTitle: str
    sourceUrl: str
    startDate: str
    startTime: str
    status: str
    taxAmount: float
    timezone: str
    totalAmount: float
    visibility: str
    voidWindowEndsAt: str


class Result(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    community: str
    externalUrl: str
    favicon: str
    indexedAt: str
    postId: str
    resultType: str
    score: int
    similarity: float


class Review(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    commentCount: int
    community: str
    externalUrl: str
    isVerified: bool
    postType: str
    rating: float
    ratingMax: float
    score: int
    tags: list[str]


class Role(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    allDay: bool
    currentUrl: str
    dateUpdated: str
    department: str
    distinctId: str
    endDate: str
    icalUid: str
    properties: Any
    recurrence: list[str]
    roleType: str
    showAs: str
    sourceTitle: str
    sourceUrl: str
    startDate: str
    status: str
    timezone: str
    title: str
    visibility: str


class Seatmap(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    aircraftCode: str
    availableSeats: int
    basicEconomyLocked: bool
    cabins: Any
    classOfService: str
    destination: str
    fareBasisCode: str
    flightNumber: str
    hasExitRow: bool
    hasFreeSeats: bool
    hasPaidSeats: bool
    origin: str
    tiers: Any
    totalSeats: int


class Service(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    description: str
    params: Any
    returns: str


class Settings(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str


class Shape(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    also: list[str]
    derived: Any
    description: str
    display: Any
    fields: Any
    groups: Any
    icon: str
    identity: list[str]
    identity_any: list[str]
    in_: Any  # in
    out: Any
    plural: str
    prefsSchemas: Any
    prior_art: Any
    shortcuts: Any


class Shelf(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    arrangement: str
    default_view: str
    icon_size: int
    isDefault: bool
    isExclusive: bool
    isPublic: bool
    itemCount: int
    listId: str
    listType: str
    member_shape: str
    ordering_mode: str
    path: str
    privacy: str
    sort_by: str


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
    applicationCategory: str
    availability: str
    barcode: str
    calories: float
    categories: list[str]
    category: str
    codename: str
    currency: str
    customizationGroups: Any
    department: str
    images: Any
    novaGroup: int
    nutritionScore: str
    originalPrice: str
    originalPriceAmount: float
    price: str
    priceAmount: float
    quantity: int
    runtimePlatform: str
    servingSize: str
    sku: str
    soldByWeight: bool
    version: str
    weight: str
    weightUnit: str
    weightValue: float


class Sound(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    bitDepth: int
    channels: int
    copyrightYear: int
    coverage: str
    dateCreated: Any
    description: str
    durationMs: int
    encoding: str
    filename: str
    format: str
    kind: str
    language: str
    license: str
    lineCount: int
    mimeType: str
    path: str
    purpose: str
    sampleRate: int
    sha: str
    size: int
    tags: list[str]


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


class Spec(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    allDay: bool
    currentUrl: str
    dateUpdated: str
    distinctId: str
    encoding: str
    endDate: str
    filename: str
    format: str
    icalUid: str
    kind: str
    labels: list[str]
    lineCount: int
    mimeType: str
    parentId: str
    path: str
    priority: int
    problem: str
    projectId: str
    properties: Any
    recurrence: list[str]
    remoteId: str
    sha: str
    showAs: str
    size: int
    sourceTitle: str
    sourceUrl: str
    startDate: str
    state: str
    status: str
    successCriteria: str
    target: Any
    targetDate: str
    timezone: str
    visibility: str


class Subscription(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    app: str
    op: str
    target: str


class Symbol(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    kind: str
    lang: str
    signature: str
    sourceLine: int
    sourcePath: str
    summary: str
    urn: str


class Tag(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    annotated: bool
    color: str
    hash: str
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
    allDay: bool
    currentUrl: str
    dateUpdated: str
    distinctId: str
    endDate: str
    icalUid: str
    labels: list[str]
    parentId: str
    priority: int
    projectId: str
    properties: Any
    recurrence: list[str]
    remoteId: str
    showAs: str
    sourceTitle: str
    sourceUrl: str
    startDate: str
    state: str
    status: str
    target: Any
    targetDate: str
    timezone: str
    visibility: str


class TaxLine(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    amount: float
    appliesToIndex: int
    code: str
    country: str
    currency: str
    description: str
    inclusive: bool
    kind: str
    merchantImposed: bool
    nature: str
    rate: float
    refundable: bool
    taxableAmount: float


class Theme(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    defaultBackgroundColor: str
    description: str
    family: str
    startMenu: str
    style: str
    themeId: str


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


class Transaction(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    allDay: bool
    amount: float
    balance: float
    category: str
    currency: str
    currentUrl: str
    dateUpdated: str
    details: Any
    distinctId: str
    endDate: str
    icalUid: str
    notes: str
    pending: bool
    postingDate: str
    properties: Any
    recurrence: list[str]
    recurring: bool
    showAs: str
    sourceTitle: str
    sourceUrl: str
    startDate: str
    status: str
    timezone: str
    type: str
    visibility: str


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
    languageConfidence: float
    segmentCount: int
    segments: Any
    sourceType: str


class Transition(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    additionalName: str
    allDay: bool
    currentUrl: str
    dateUpdated: str
    distinctId: str
    endDate: str
    familyName: str
    gender: str
    givenName: str
    honorificPrefix: str
    honorificSuffix: str
    icalUid: str
    legalName: str
    maidenName: str
    nameOrder: str
    nickname: str
    phoneticFamilyName: str
    phoneticGivenName: str
    properties: Any
    recurrence: list[str]
    showAs: str
    sortAs: str
    sourceTitle: str
    sourceUrl: str
    startDate: str
    status: str
    timezone: str
    visibility: str


class Trip(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    allDay: bool
    arrivalTime: str
    bookingToken: str
    cabinClass: str
    carbonEmissions: Any
    currency: str
    currentUrl: str
    dateUpdated: str
    departureTime: str
    distance: str
    distinctId: str
    duration: str
    durationMinutes: int
    endDate: str
    fare: str
    fareAmount: float
    guest: Any
    icalUid: str
    isPool: bool
    isReserve: bool
    isScheduled: bool
    isSurge: bool
    marketplace: str
    properties: Any
    rating: str
    recurrence: list[str]
    showAs: str
    sourceTitle: str
    sourceUrl: str
    startDate: str
    status: str
    stops: int
    timezone: str
    trackingUrl: str
    tripType: str
    vehicle: Any
    vehicleType: str
    visibility: str


class Unit(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    iso4217: str
    iso4217Numeric: str
    kind: str
    label: str
    logBase: float
    minorExponent: int
    qudtUnitIri: str
    siDigitalFrameworkUri: str
    symbol: str
    toBaseFactor: float
    toBaseOffset: float
    ucumCode: str
    unCefactCommonCode: str
    wikidataId: str


class User(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    actorType: str
    osUsername: str
    primaryUser: bool


class UserIdentity(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    active: bool
    person_node_id: str
    user_id: str
    volume_id: str


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
    copyrightYear: int
    coverage: str
    dateCreated: Any
    description: str
    durationMs: int
    encoding: str
    filename: str
    format: str
    frameRate: float
    kind: str
    language: str
    license: str
    lineCount: int
    mimeType: str
    path: str
    resolution: str
    sha: str
    size: int
    tags: list[str]
    viewCount: int


class Volume(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    address: str
    auto_mount: bool
    default_view: str
    ejectable: bool
    freeBytes: int
    icon: str
    kind: str
    provider: str
    readOnly: bool
    removable: bool
    scope: str
    source: str
    totalBytes: int
    volume_id: str


class Vote(TypedDict, total=False):
    id: str
    name: str
    text: str
    url: str
    image: str
    author: str
    datePublished: str
    content: str
    direction: str
    instance: str
    note: str


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
    favicon: str
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
    status: str
    versionId: str


# Structured shape defs — consumed by the app worker to attach
# `__shape_def__` on every @returns(shape) response. Wire-equivalent
# to `agentos_graph::ShapeDef`.
SHAPE_DEFS: dict[str, dict] = {
    'account': {'name': 'account', 'plural': 'accounts', 'description': "A user's presence within a namespace — their GitHub handle, Gmail address,", 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'accountType', 'ty': 'string'}, {'name': 'bio', 'ty': 'text'}, {'name': 'color', 'ty': 'string'}, {'name': 'display', 'ty': 'string'}, {'name': 'displayName', 'ty': 'string'}, {'name': 'email', 'ty': 'string'}, {'name': 'handle', 'ty': 'string'}, {'name': 'identifier', 'ty': 'string', 'required': True}, {'name': 'isActive', 'ty': 'boolean'}, {'name': 'issuer', 'ty': 'string'}, {'name': 'joinedDate', 'ty': 'datetime'}, {'name': 'lastActive', 'ty': 'datetime'}, {'name': 'lastProfileFetch', 'ty': 'datetime'}, {'name': 'metadata', 'ty': 'json'}, {'name': 'phone', 'ty': 'string'}, {'name': 'userId', 'ty': 'string'}], 'identity': ['at', 'identifier'], 'display': {'subtitle': 'identifier'}, 'groups': [{'name': 'Identity', 'fields': ['identifier', 'handle', 'displayName', 'email', 'phone']}, {'name': 'Profile', 'fields': ['bio', 'accountType', 'color', 'isActive']}, {'name': 'Activity', 'fields': ['joinedDate', 'lastActive', 'lastProfileFetch']}, {'name': 'Technical', 'fields': ['userId', 'issuer', 'metadata']}], 'prior_art': [{'source': 'ActivityPub Actor model', 'url': 'https://www.w3.org/TR/activitypub/', 'notes': 'Account id is a URL; Server/Application/Operator are separate Actor objects. We adopt the same separation but ground each in graph nodes rather than URLs, so node lifecycle (rebrand, merge) propagates to all referencing accounts.'}, {'source': 'schema.org Offer.seller union', 'url': 'https://schema.org/Offer', 'notes': 'seller: Person | Organization. The `actor` shape (which `at` and `operator` target) is our existing union of person/org/agent — same pattern.'}, {'source': 'OpenID Connect Core 1.0 (`iss`/`sub`)', 'url': 'https://openid.net/specs/openid-connect-core-1_0.html', 'notes': "OIDC keeps issuer as opaque URL because there's no shared graph across token issuers. We have a graph; we replace the URL with a graph node, gaining mutability and traversal at the cost of requiring a node to exist before an account can reference it. Trade is worth it."}, {'source': 'WebFinger (RFC 7033)', 'url': 'https://datatracker.ietf.org/doc/html/rfc7033', 'notes': "Resolves issuer+identifier pairs to profile metadata. Our identifier aligns with WebFinger's acct: URI scheme (user@host), but the `host` part becomes a graph node (not a string)."}, {'source': 'vCard 4.0 (RFC 6350)', 'url': 'https://datatracker.ietf.org/doc/html/rfc6350', 'notes': "Defines displayName/email/phone/org in contact cards. We adopt vCard's contact semantics for the human-readable fields."}]},
    'activity': {'name': 'activity', 'plural': 'activities', 'description': 'An immutable change event — a graph mutation, app run, search, or load.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'action', 'ty': 'string'}, {'name': 'allDay', 'ty': 'boolean'}, {'name': 'changedKeys', 'ty': 'stringlist'}, {'name': 'currentUrl', 'ty': 'string'}, {'name': 'dateUpdated', 'ty': 'datetime'}, {'name': 'distinctId', 'ty': 'string'}, {'name': 'duration', 'ty': 'number'}, {'name': 'endDate', 'ty': 'datetime'}, {'name': 'icalUid', 'ty': 'string'}, {'name': 'properties', 'ty': 'json'}, {'name': 'recurrence', 'ty': 'stringlist'}, {'name': 'showAs', 'ty': 'string'}, {'name': 'sourceTitle', 'ty': 'string'}, {'name': 'sourceUrl', 'ty': 'url'}, {'name': 'startDate', 'ty': 'datetime'}, {'name': 'status', 'ty': 'string'}, {'name': 'success', 'ty': 'boolean'}, {'name': 'timezone', 'ty': 'string'}, {'name': 'toolName', 'ty': 'string'}, {'name': 'visibility', 'ty': 'string'}], 'also': ['event'], 'display': {'subtitle': 'action', 'highlights': ['startDate', 'endDate', 'location']}, 'prior_art': [{'source': 'ActivityStreams 2.0', 'url': 'https://www.w3.org/TR/activitystreams-core/', 'notes': "AS2's Create/Update/Delete activities match our action values. We diverge by tracking changedKeys explicitly instead of encoding full object replacement."}, {'source': 'OpenTelemetry Traces', 'url': 'https://opentelemetry.io/docs/concepts/signals/traces/', 'notes': 'Closest fit for toolName/duration/success — span-shaped. Our activity is closer to a span event than a full span.'}]},
    'actor': {'name': 'actor', 'plural': 'actors', 'description': 'Base type for anything that can be attributed as "who did this" in the graph.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'actorType', 'ty': 'string'}], 'display': {'subtitle': 'actorType'}, 'prior_art': [{'source': 'FOAF Agent', 'url': 'http://xmlns.com/foaf/spec/#term_Agent', 'notes': "FOAF Agent is the base class for Person, Organization, and Group. Our actorType mirrors FOAF's agent taxonomy."}, {'source': 'ActivityStreams 2.0 Actor', 'url': 'https://www.w3.org/TR/activitystreams-vocabulary/#actor-types', 'notes': 'AS2 defines Actor types (Person, Organization, Group, Service, Application). Our agent ≈ Service/Application.'}]},
    'aircraft': {'name': 'aircraft', 'plural': 'aircraft', 'description': 'An aircraft type (not an individual plane). Linked from flight search results.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'aisle', 'ty': 'string'}, {'name': 'availability', 'ty': 'string'}, {'name': 'barcode', 'ty': 'string'}, {'name': 'calories', 'ty': 'number'}, {'name': 'categories', 'ty': 'stringlist'}, {'name': 'category', 'ty': 'string'}, {'name': 'currency', 'ty': 'string'}, {'name': 'customizationGroups', 'ty': 'json'}, {'name': 'department', 'ty': 'string'}, {'name': 'iataCode', 'ty': 'string'}, {'name': 'icaoCode', 'ty': 'string', 'required': True}, {'name': 'images', 'ty': 'json'}, {'name': 'model', 'ty': 'string'}, {'name': 'novaGroup', 'ty': 'integer'}, {'name': 'nutritionScore', 'ty': 'string'}, {'name': 'originalPrice', 'ty': 'string'}, {'name': 'originalPriceAmount', 'ty': 'number'}, {'name': 'price', 'ty': 'string'}, {'name': 'priceAmount', 'ty': 'number'}, {'name': 'quantity', 'ty': 'integer'}, {'name': 'rangeKm', 'ty': 'integer'}, {'name': 'seatCapacity', 'ty': 'integer'}, {'name': 'servingSize', 'ty': 'string'}, {'name': 'sku', 'ty': 'string'}, {'name': 'soldByWeight', 'ty': 'boolean'}, {'name': 'variant', 'ty': 'string'}, {'name': 'weight', 'ty': 'string'}, {'name': 'weightUnit', 'ty': 'string'}, {'name': 'weightValue', 'ty': 'number'}], 'also': ['product'], 'identity': ['icaoCode'], 'display': {'subtitle': 'model'}, 'prior_art': [{'source': 'ICAO Aircraft Type Designators (Doc 8643)', 'url': 'https://www.icao.int/publications/DOC8643/Pages/Search.aspx', 'notes': 'Our icaoCode is the canonical 4-char type code (B738, A320); iataCode is the 3-char IATA equivalent (738, 320).'}, {'source': 'schema.org/Vehicle', 'url': 'https://schema.org/Vehicle', 'notes': 'Our model/seatCapacity map to vehicleModelDate/vehicleSeatingCapacity; manufacturer matches directly.'}]},
    'airline': {'name': 'airline', 'plural': 'airlines', 'description': 'A commercial airline. Created from flight search results.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'actorType', 'ty': 'string'}, {'name': 'alliance', 'ty': 'string'}, {'name': 'callsign', 'ty': 'string'}, {'name': 'country', 'ty': 'string'}, {'name': 'iataCode', 'ty': 'string', 'required': True}, {'name': 'icaoCode', 'ty': 'string'}, {'name': 'industry', 'ty': 'string'}], 'also': ['organization'], 'identity': ['iataCode'], 'display': {'subtitle': 'iataCode', 'image': 'image', 'highlights': ['headquarters']}, 'prior_art': [{'source': 'IATA Airline Designators', 'url': 'https://www.iata.org/en/publications/directories/code-search/', 'notes': 'iataCode is 2-letter (UA, DL); icaoCode is 3-letter (UAL, DAL); callsign is radio callsign (UNITED). Full IATA/ICAO alignment.'}, {'source': 'schema.org/Airline', 'url': 'https://schema.org/Airline', 'notes': "schema.org's Airline is an Organization subtype. Our alliance is a free field; schema.org doesn't model it."}]},
    'airport': {'name': 'airport', 'plural': 'airports', 'description': 'An airport. Created from flight search results and linked to flights.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'city', 'ty': 'string'}, {'name': 'country', 'ty': 'string'}, {'name': 'countryCode', 'ty': 'string'}, {'name': 'elevationFt', 'ty': 'integer'}, {'name': 'iataCode', 'ty': 'string', 'required': True}, {'name': 'icaoCode', 'ty': 'string'}, {'name': 'terminalCount', 'ty': 'integer'}, {'name': 'timezone', 'ty': 'string'}], 'identity': ['iataCode'], 'display': {'subtitle': 'iataCode'}, 'prior_art': [{'source': 'IATA/ICAO Airport Codes', 'url': 'https://www.iata.org/en/publications/directories/code-search/', 'notes': 'iataCode is 3-letter (LAX, JFK); icaoCode is 4-letter (KLAX, KJFK). Canonical identifiers for global airport routing.'}, {'source': 'schema.org/Airport', 'url': 'https://schema.org/Airport', 'notes': 'Our iataCode/icaoCode = iataCode/icaoCode; city/country = address fields; elevationFt ≈ elevation. Direct alignment.'}, {'source': 'OurAirports open dataset', 'url': 'https://ourairports.com/data/', 'notes': 'Practical open dataset covering terminalCount, elevation, and country codes (ISO 3166-1) aligning with our countryCode field.'}]},
    'app': {'name': 'app', 'plural': 'apps', 'description': 'An application — the one installable, launchable unit. System apps', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'account', 'ty': 'json'}, {'name': 'color', 'ty': 'string'}, {'name': 'composition', 'ty': 'json'}, {'name': 'defaultRoute', 'ty': 'string'}, {'name': 'defaultView', 'ty': 'string'}, {'name': 'description', 'ty': 'text'}, {'name': 'error', 'ty': 'text'}, {'name': 'handles', 'ty': 'stringlist'}, {'name': 'iconRole', 'ty': 'string'}, {'name': 'isSystem', 'ty': 'boolean'}, {'name': 'route', 'ty': 'string'}, {'name': 'status', 'ty': 'string'}], 'identity': ['id'], 'display': {'subtitle': 'description'}, 'prior_art': [{'source': 'macOS .app bundle (Info.plist)', 'url': 'https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFBundles/BundleTypes/BundleTypes.html', 'notes': 'CFBundleIdentifier ≈ id; CFBundleName ≈ name; CFBundleIconFile ≈ iconRole (we use a role rather than a file path so themes can override).'}, {'source': 'freedesktop .desktop entry', 'url': 'https://specifications.freedesktop.org/desktop-entry-spec/latest/', 'notes': 'Name, Icon, Exec — the Linux/XDG peer. We model the launchable surface, not the executable (the engine knows how to spawn).'}, {'source': 'Windows AppUserModelID', 'url': 'https://learn.microsoft.com/en-us/windows/win32/shell/appids', 'notes': 'Stable per-app identity decoupled from the executable on disk. Our `id` plays the same role — themes and bookmarks reference it, the binary is an implementation detail of seed_system_apps().'}, {'source': 'Model Context Protocol (MCP) — Server', 'url': 'https://modelcontextprotocol.io/specification', 'notes': 'An installed app = an MCP-registerable provider. id ≈ MCP server name; status tracks connection lifecycle.'}, {'source': 'OpenAPI 3.1 (Info + Servers)', 'url': 'https://spec.openapis.org/oas/v3.1.0', 'notes': 'Our description/online_at/privacy_at/terms_at ≈ OpenAPI info.description/info.termsOfService/contact.'}]},
    'auth_challenge': {'name': 'auth_challenge', 'plural': 'auth_challenges', 'description': 'A platform demands something only a human (usually) can do — scan a QR', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'artifact', 'ty': 'text'}, {'name': 'continueWith', 'ty': 'string'}, {'name': 'expiresAt', 'ty': 'datetime'}, {'name': 'instructions', 'ty': 'text'}, {'name': 'kind', 'ty': 'string'}, {'name': 'payload', 'ty': 'string'}, {'name': 'retrieval', 'ty': 'json'}], 'display': {'subtitle': 'instructions', 'body': 'artifact', 'mono': 'artifact'}, 'prior_art': [{'source': 'OAuth 2.0 Device Authorization Grant (RFC 8628)', 'url': 'https://datatracker.ietf.org/doc/html/rfc8628', 'notes': 'The device flow returns the human-must-act moment as data, not as an error: user_code + verification_uri + expires_in, with the client polling the token endpoint until the human acts. Same anatomy here — payload/artifact ≈ user_code/verification_uri, expiresAt ≈ expires_in, continueWith ≈ the polling step.'}, {'source': 'whatsapp-web.js + qrcode-terminal', 'url': 'https://github.com/pedroslopez/whatsapp-web.js', 'notes': 'The proven precedent for QR-as-text: the linked-device QR payload is re-rendered as Unicode block characters in a terminal and scanned straight off the screen. `artifact` generalizes that to every text surface.'}]},
    'birth': {'name': 'birth', 'plural': 'births', 'description': "A person's birth. The canonical event recording given/family names,", 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'additionalName', 'ty': 'string'}, {'name': 'allDay', 'ty': 'boolean'}, {'name': 'currentUrl', 'ty': 'string'}, {'name': 'dateUpdated', 'ty': 'datetime'}, {'name': 'distinctId', 'ty': 'string'}, {'name': 'endDate', 'ty': 'datetime'}, {'name': 'familyName', 'ty': 'string'}, {'name': 'gender', 'ty': 'string'}, {'name': 'givenName', 'ty': 'string'}, {'name': 'honorificPrefix', 'ty': 'string'}, {'name': 'honorificSuffix', 'ty': 'string'}, {'name': 'icalUid', 'ty': 'string'}, {'name': 'legalName', 'ty': 'string'}, {'name': 'maidenName', 'ty': 'string'}, {'name': 'nameOrder', 'ty': 'string'}, {'name': 'nickname', 'ty': 'string'}, {'name': 'phoneticFamilyName', 'ty': 'string'}, {'name': 'phoneticGivenName', 'ty': 'string'}, {'name': 'properties', 'ty': 'json'}, {'name': 'recurrence', 'ty': 'stringlist'}, {'name': 'showAs', 'ty': 'string'}, {'name': 'sortAs', 'ty': 'string'}, {'name': 'sourceTitle', 'ty': 'string'}, {'name': 'sourceUrl', 'ty': 'url'}, {'name': 'startDate', 'ty': 'datetime'}, {'name': 'status', 'ty': 'string'}, {'name': 'timezone', 'ty': 'string'}, {'name': 'visibility', 'ty': 'string'}], 'also': ['event'], 'display': {'subtitle': 'location', 'highlights': ['startDate', 'location']}, 'prior_art': [{'source': 'schema.org/Person.birthDate / birthPlace', 'url': 'https://schema.org/birthDate', 'notes': 'schema.org collapses birth into two flat fields on Person; we lift to an event-node so all birth particulars (name, gender, legal-doc form) co-locate per platform README rule 1.'}, {'source': 'GEDCOM 7 INDI.BIRT', 'url': 'https://gedcom.io/specifications/FamilySearchGEDCOMv7.html', 'notes': "Genealogy's canonical model: a typed INDIVIDUAL_EVENT with DATE, PLAC, ADDR sub-records. Our `birth` shape is the equivalent — sub-records map to event-base fields (startDate, location) plus the typed birth-particulars fields above."}, {'source': 'GEDCOM-X Fact (FactType=Birth)', 'url': 'https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md', 'notes': "FamilySearch's reified-fact model. We adopt the reified-event pattern; field set is richer (legalName + phonetics + nameOrder) for present-day identity-document interop."}]},
    'book': {'name': 'book', 'plural': 'books', 'description': 'A book. Books are BOTH creative works (the intellectual work — its', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'aisle', 'ty': 'string'}, {'name': 'availability', 'ty': 'string'}, {'name': 'awardsWon', 'ty': 'stringlist'}, {'name': 'barcode', 'ty': 'string'}, {'name': 'calories', 'ty': 'number'}, {'name': 'categories', 'ty': 'stringlist'}, {'name': 'category', 'ty': 'string'}, {'name': 'characters', 'ty': 'stringlist'}, {'name': 'copyrightYear', 'ty': 'integer'}, {'name': 'coverage', 'ty': 'string'}, {'name': 'currency', 'ty': 'string'}, {'name': 'customizationGroups', 'ty': 'json'}, {'name': 'dateCreated', 'ty': 'date'}, {'name': 'department', 'ty': 'string'}, {'name': 'description', 'ty': 'string'}, {'name': 'format', 'ty': 'string'}, {'name': 'genres', 'ty': 'stringlist'}, {'name': 'images', 'ty': 'json'}, {'name': 'isbn', 'ty': 'string'}, {'name': 'isbn13', 'ty': 'string'}, {'name': 'language', 'ty': 'string'}, {'name': 'license', 'ty': 'string'}, {'name': 'novaGroup', 'ty': 'integer'}, {'name': 'nutritionScore', 'ty': 'string'}, {'name': 'originalPrice', 'ty': 'string'}, {'name': 'originalPriceAmount', 'ty': 'number'}, {'name': 'originalTitle', 'ty': 'string'}, {'name': 'pages', 'ty': 'integer'}, {'name': 'places', 'ty': 'stringlist'}, {'name': 'price', 'ty': 'string'}, {'name': 'priceAmount', 'ty': 'number'}, {'name': 'quantity', 'ty': 'integer'}, {'name': 'series', 'ty': 'string'}, {'name': 'servingSize', 'ty': 'string'}, {'name': 'sku', 'ty': 'string'}, {'name': 'soldByWeight', 'ty': 'boolean'}, {'name': 'tags', 'ty': 'stringlist'}, {'name': 'weight', 'ty': 'string'}, {'name': 'weightUnit', 'ty': 'string'}, {'name': 'weightValue', 'ty': 'number'}], 'also': ['creative_work', 'product'], 'identity_any': ['isbn13', 'isbn'], 'display': {'subtitle': 'written_by', 'image': 'image', 'body': 'description', 'highlights': ['datePublished', 'published_by']}, 'prior_art': [{'source': 'schema.org/Book', 'url': 'https://schema.org/Book', 'notes': 'Our isbn maps to isbn; writtenBy = author; publisher matches; pages = numberOfPages; language = inLanguage; format ≈ bookFormat (Hardcover/Paperback/EBook).'}, {'source': 'ONIX for Books 3.0', 'url': 'https://www.editeur.org/83/Overview/', 'notes': 'Publishing-industry canonical. Our isbn/isbn13/pages/format/language/series/originalTitle align with ONIX Product Identifier, Extent, ProductForm, Language, Collection, and OriginalLanguageTitle composites.'}, {'source': 'Open Library Books API', 'url': 'https://openlibrary.org/developers/api', 'notes': 'Practical lookup by ISBN. Our genres/characters/places/awardsWon map to subjects/subject_people/subject_places/subject_times (awards less standardized).'}]},
    'booking_offer': {'name': 'booking_offer', 'plural': 'booking_offers', 'description': 'A signed, itemized, fully-priced commitment presented to a human for', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'allDay', 'ty': 'boolean'}, {'name': 'approvedAt', 'ty': 'datetime'}, {'name': 'baseAmount', 'ty': 'number'}, {'name': 'blob', 'ty': 'string'}, {'name': 'cartId', 'ty': 'string', 'required': True}, {'name': 'checkoutUrl', 'ty': 'url'}, {'name': 'conditions', 'ty': 'json'}, {'name': 'confirmEndpoint', 'ty': 'url'}, {'name': 'contactEmail', 'ty': 'string'}, {'name': 'contactPhone', 'ty': 'string'}, {'name': 'currency', 'ty': 'string'}, {'name': 'currentUrl', 'ty': 'string'}, {'name': 'dateUpdated', 'ty': 'datetime'}, {'name': 'distinctId', 'ty': 'string'}, {'name': 'endDate', 'ty': 'datetime'}, {'name': 'expiresAt', 'ty': 'datetime'}, {'name': 'feesAmount', 'ty': 'number'}, {'name': 'hasVoidWindow', 'ty': 'boolean'}, {'name': 'icalUid', 'ty': 'string'}, {'name': 'isChangeable', 'ty': 'boolean'}, {'name': 'isRefundable', 'ty': 'boolean'}, {'name': 'itineraryHash', 'ty': 'string'}, {'name': 'preparedAt', 'ty': 'datetime'}, {'name': 'presentedAt', 'ty': 'datetime'}, {'name': 'properties', 'ty': 'json'}, {'name': 'recurrence', 'ty': 'stringlist'}, {'name': 'referenceNumber', 'ty': 'string'}, {'name': 'review', 'ty': 'string'}, {'name': 'showAs', 'ty': 'string'}, {'name': 'signature', 'ty': 'string'}, {'name': 'signatureAlg', 'ty': 'string'}, {'name': 'signedBy', 'ty': 'string'}, {'name': 'sourceTitle', 'ty': 'string'}, {'name': 'sourceUrl', 'ty': 'url'}, {'name': 'startDate', 'ty': 'datetime'}, {'name': 'status', 'ty': 'string'}, {'name': 'taxAmount', 'ty': 'number'}, {'name': 'timezone', 'ty': 'string'}, {'name': 'totalAmount', 'ty': 'number'}, {'name': 'visibility', 'ty': 'string'}, {'name': 'voidWindowEndsAt', 'ty': 'datetime'}], 'also': ['event'], 'identity': ['at', 'cartId'], 'display': {'subtitle': 'totalAmount', 'highlights': ['startDate', 'endDate', 'location']}, 'prior_art': [{'source': 'Duffel Offers API (pre-Order priced shape)', 'url': 'https://duffel.com/docs/api/offers/schema', 'notes': 'Duffel\'s Offer is the "priced, held, about-to-become-an-order" state. Our baseAmount/taxAmount/totalAmount/currency map to Duffel\'s base_amount/tax_amount/total_amount/total_currency; expiresAt = offer.expires_at. Duffel rolls taxes into a single aggregate — we split them into tax_line[] nodes.'}, {'source': 'IATA NDC OfferPriceRQ / OfferPriceRS', 'url': 'https://developer.iata.org/en/ndc/', 'notes': 'NDC\'s OfferPrice is the mandatory "price this exact shape with these exact passengers" step between Shop and OrderCreate. Our guests[] mirror NDC\'s PaxList; taxLines[] mirror Taxes/ TaxSummary; signature mirrors OfferPriceRS\'s ShoppingResponseID that the airline expects back on OrderCreateRQ.'}, {'source': 'Stripe Checkout Session', 'url': 'https://docs.stripe.com/api/checkout/sessions/object', 'notes': 'Canonical "about-to-charge" object. Our cartId ≈ session.id; expiresAt ≈ session.expires_at; totalAmount ≈ session.amount_total; paymentMethod relation mirrors session.payment_method. Stripe assumes line_item shape; we use domain-specific relations (trips/reservedItems) instead.'}, {'source': 'Shopify Draft Order', 'url': 'https://shopify.dev/docs/api/admin-graphql/latest/objects/DraftOrder', 'notes': 'Shopify\'s non-binding pre-order — validates the "cart with a reference number that can be invoiced and converted" pattern. Our referenceNumber ≈ DraftOrder.name; becameReservation / becameTransaction mirror DraftOrder -> Order conversion.'}, {'source': 'WebAuthn clientDataJSON + signed assertion', 'url': 'https://www.w3.org/TR/webauthn-3/', 'notes': 'Precedent for "the thing the user saw is what got signed." WebAuthn signs (challenge, origin, type); we sign (cartId, itineraryHash, total, expiresAt). Our itineraryHash plays the role of WebAuthn\'s challenge — a commitment the verifier can match against the submitted shape.'}, {'source': 'CoinGate Invoice (short-TTL priced blob)', 'url': 'https://developer.coingate.com/reference/order-statuses', 'notes': 'Validates the short-TTL pattern outside airlines. CoinGate invoices carry id, price locked ~20 min, and status (new, pending, paid, expired, canceled). Our status enum matches — pre-commit objects need expiry as a first-class terminal.'}, {'source': 'schema.org/Order + schema.org/Invoice', 'url': 'https://schema.org/Order', 'notes': 'schema.org models Offer -> Order -> Invoice. booking_offer sits between Offer and Order — a priced, itemized, signed proposal awaiting explicit human commit. Our baseAmount + taxAmount + totalAmount align with UBL 2.1 LegalMonetaryTotal.'}]},
    'bookmark': {'name': 'bookmark', 'plural': 'bookmarks', 'description': 'A pointer into the graph — the universal shortcut. A bookmark is a', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'address', 'ty': 'string'}, {'name': 'handle', 'ty': 'string'}], 'identity': ['points_to'], 'display': {'subtitle': 'name'}, 'prior_art': [{'source': 'Browser bookmarks (Mosaic / Netscape Navigator hotlist)', 'url': 'https://en.wikipedia.org/wiki/Bookmark_(digital)', 'notes': "Direct precedent. A bookmark is a name + a target; the target is the contract; the surface doesn't care what's behind it. We replace HTTP URLs with graph node references; everything else maps 1:1."}, {'source': 'macOS alias / Windows .lnk file', 'url': 'https://en.wikipedia.org/wiki/Alias_(Mac_OS)', 'notes': 'OS-level shortcut primitive. Same shape: name + target. Per- instance position is handled by the parent folder/desktop in both — for us that lives on the contains-link.'}, {'source': 'Finder sidebar / Windows Explorer Quick Access', 'url': 'https://support.apple.com/guide/mac-help/customize-the-finder-sidebar-mchlp3014/mac', 'notes': 'OS file managers use a bookmark sidebar as their universal navigation primitive (My Computer, Documents, Network). We treat every shape the same way — bookmark to any graph node, no FS bias.'}]},
    'branch': {'name': 'branch', 'plural': 'branches', 'description': 'A git branch.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'ahead', 'ty': 'integer'}, {'name': 'behind', 'ty': 'integer'}, {'name': 'commit', 'ty': 'string'}, {'name': 'isCurrent', 'ty': 'boolean'}, {'name': 'isRemote', 'ty': 'boolean'}, {'name': 'upstream', 'ty': 'string'}], 'display': {'subtitle': 'commit'}, 'prior_art': [{'source': 'Git Internals — Branches', 'url': 'https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell', 'notes': 'A branch is a movable pointer to a commit. Our commit field is the HEAD sha; ahead/behind mirror `git rev-list --count`.'}, {'source': 'GitHub REST — branches', 'url': 'https://docs.github.com/en/rest/branches/branches', 'notes': 'Practical API surface. Our upstream ≈ the remote tracking ref; we flatten protection/commit metadata that GitHub nests.'}]},
    'brand': {'name': 'brand', 'plural': 'brands', 'description': 'A consumer brand — a named, visual, commercial identity. Often (but not', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string', 'required': True}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'country', 'ty': 'string'}, {'name': 'primaryColor', 'ty': 'string'}, {'name': 'tagline', 'ty': 'string'}, {'name': 'textColor', 'ty': 'string'}], 'identity': ['url'], 'display': {'subtitle': 'tagline'}, 'prior_art': [{'source': 'schema.org/Brand', 'url': 'https://schema.org/Brand', 'notes': "Our tagline ≈ slogan; founded = foundingDate; ownedBy ≈ parentOrganization (on the owning Organization); logo = logo. schema.org doesn't model color on Brand; that's a Wikidata extension."}, {'source': 'Wikidata (Brand, Q431289)', 'url': 'https://www.wikidata.org/wiki/Q431289', 'notes': 'Cross-reference identity for dedupe. country maps to P17 (country); founded to P571 (inception); ownedBy to P127 (owned by); primaryColor ≈ P465 "hex color code" (Wikidata stores without the "#" prefix — we include it to match CSS and our app-frontmatter convention).'}, {'source': 'Apple PassKit pkpass', 'url': 'https://developer.apple.com/documentation/walletpasses', 'notes': 'Wallet passes carry backgroundColor / foregroundColor / labelColor — three-color palette aligned with our primaryColor / textColor. We ship two here (pairing primary with its paired text color) and defer the third until a renderer needs it. An itinerary PDF can derive a "label" color from a lighter tint of textColor at render time if needed, rather than fixing it at the data layer.'}, {'source': 'Material Design 3 — dynamic color roles', 'url': 'https://m3.material.io/styles/color/roles', 'notes': "Material's palette has paired slots (`primary` / `onPrimary`; `secondary` / `onSecondary`; `surface` / `onSurface`). Our primaryColor/textColor follows the primary/onPrimary pairing. Secondary tiers are deferred until renderers actually need them."}]},
    'calendar': {'name': 'calendar', 'plural': 'calendars', 'description': 'A calendar — container for events.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'accessRole', 'ty': 'string'}, {'name': 'backgroundColor', 'ty': 'string'}, {'name': 'calendarId', 'ty': 'string', 'required': True}, {'name': 'color', 'ty': 'string'}, {'name': 'foregroundColor', 'ty': 'string'}, {'name': 'isPrimary', 'ty': 'boolean'}, {'name': 'isReadonly', 'ty': 'boolean'}, {'name': 'source', 'ty': 'string'}, {'name': 'timezone', 'ty': 'string'}], 'identity': ['at', 'calendarId'], 'display': {'subtitle': 'source'}, 'prior_art': [{'source': 'RFC 5545 VCALENDAR', 'url': 'https://datatracker.ietf.org/doc/html/rfc5545', 'notes': "Our calendarId ≈ VCALENDAR's X-WR-CALID; timezone = X-WR-TIMEZONE; events relation mirrors VCALENDAR's VEVENT components."}, {'source': 'CalDAV (RFC 4791)', 'url': 'https://datatracker.ietf.org/doc/html/rfc4791', 'notes': 'CalDAV calendar collections define accessRole semantics (owner/writer/reader) that match our field directly.'}, {'source': 'Google Calendar API CalendarList', 'url': 'https://developers.google.com/calendar/api/v3/reference/calendarList', 'notes': "Practical API mirror. Our color/backgroundColor/foregroundColor, isPrimary, accessRole come from Google's CalendarList resource."}]},
    'channel': {'name': 'channel', 'plural': 'channels', 'description': 'A content channel — typically a YouTube channel. Videos are uploaded to channels.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'banner', 'ty': 'url'}, {'name': 'subscriberCount', 'ty': 'integer'}], 'identity': ['at', 'id'], 'display': {'subtitle': 'subscriberCount'}, 'prior_art': [{'source': 'ActivityStreams 2.0 Collection', 'url': 'https://www.w3.org/TR/activitystreams-vocabulary/#dfn-collection', 'notes': "A channel is a platform-specific Collection of media items. Our banner is channel branding; AS2 doesn't model that directly."}, {'source': 'YouTube Data API — Channel resource', 'url': 'https://developers.google.com/youtube/v3/docs/channels', 'notes': "Practical source. Our channel id/banner map to YouTube's channelId and brandingSettings.image.bannerExternalUrl."}, {'source': 'RSS 2.0 <channel>', 'url': 'https://www.rssboard.org/rss-specification', 'notes': 'Original "channel" concept — a grouped feed with title, image, and items. Our channel is the same pattern for video.'}]},
    'class': {'name': 'class', 'plural': 'classes', 'description': 'A scheduled, bookable group activity — gym classes, workshops, courses.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'activityType', 'ty': 'string'}, {'name': 'allDay', 'ty': 'boolean'}, {'name': 'capacity', 'ty': 'integer'}, {'name': 'currentUrl', 'ty': 'string'}, {'name': 'dateUpdated', 'ty': 'datetime'}, {'name': 'distinctId', 'ty': 'string'}, {'name': 'endDate', 'ty': 'datetime'}, {'name': 'icalUid', 'ty': 'string'}, {'name': 'isFull', 'ty': 'boolean'}, {'name': 'properties', 'ty': 'json'}, {'name': 'recurrence', 'ty': 'stringlist'}, {'name': 'showAs', 'ty': 'string'}, {'name': 'sourceTitle', 'ty': 'string'}, {'name': 'sourceUrl', 'ty': 'url'}, {'name': 'spotsRemaining', 'ty': 'integer'}, {'name': 'startDate', 'ty': 'datetime'}, {'name': 'status', 'ty': 'string'}, {'name': 'timezone', 'ty': 'string'}, {'name': 'visibility', 'ty': 'string'}], 'also': ['event'], 'display': {'subtitle': 'activityType', 'highlights': ['startDate', 'endDate', 'location']}, 'prior_art': [{'source': 'schema.org/EducationEvent', 'url': 'https://schema.org/EducationEvent', 'notes': "schema.org's closest peer for a bookable class. Our instructor = performer; capacity = maximumAttendeeCapacity; spotsRemaining ≈ remainingAttendeeCapacity."}, {'source': 'schema.org/ExerciseAction', 'url': 'https://schema.org/ExerciseAction', 'notes': 'Fitness-specific vocabulary: activityType ≈ exerciseType; venue matches directly as location.'}, {'source': 'Mindbody Public API (class schedules)', 'url': 'https://developers.mindbodyonline.com/PublicDocumentation/V6', 'notes': "Practical API mirror. Our capacity/spotsRemaining/isFull come from Mindbody's MaxCapacity/TotalBooked/IsWaitlistAvailable."}]},
    'community': {'name': 'community', 'plural': 'communities', 'description': 'An online community — a subreddit, Facebook group, or similar.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'allowCrypto', 'ty': 'boolean'}, {'name': 'memberCount', 'ty': 'integer'}, {'name': 'privacy', 'ty': 'string'}, {'name': 'subscriberCount', 'ty': 'integer'}], 'identity': ['at', 'id'], 'display': {'subtitle': 'text'}, 'prior_art': [{'source': 'ActivityPub Group Actor', 'url': 'https://www.w3.org/TR/activitypub/', 'notes': 'AP Group Actor models shared-inbox communities (Lemmy, Kbin, Mbin). Our privacy ≈ audience/to visibility.'}, {'source': 'schema.org/Organization', 'url': 'https://schema.org/Organization', 'notes': 'A community-as-organization is a loose fit; privacy has no direct schema.org property.'}, {'source': 'Reddit API — Subreddit', 'url': 'https://www.reddit.com/dev/api/#GET_subreddits_where', 'notes': 'Practical source. Our privacy ≈ subreddit_type (public/private/ restricted); text ≈ public_description.'}]},
    'conversation': {'name': 'conversation', 'plural': 'conversations', 'description': 'A message thread — an iMessage chat, WhatsApp group, email thread, Claude', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'accountEmail', 'ty': 'string'}, {'name': 'cwd', 'ty': 'string'}, {'name': 'gitBranch', 'ty': 'string'}, {'name': 'historyId', 'ty': 'string'}, {'name': 'isArchived', 'ty': 'boolean'}, {'name': 'isGroup', 'ty': 'boolean'}, {'name': 'messageCount', 'ty': 'integer'}, {'name': 'source', 'ty': 'string'}, {'name': 'unreadCount', 'ty': 'integer'}], 'identity': ['at', 'id'], 'display': {'subtitle': 'text'}, 'prior_art': [{'source': 'ActivityStreams 2.0 context/inReplyTo', 'url': 'https://www.w3.org/TR/activitystreams-vocabulary/#dfn-context', 'notes': 'Conversations are AS2 contexts — the thread that groups replies. Our participant[] ≈ to/cc/audience.'}, {'source': 'Matrix Room (m.room)', 'url': 'https://spec.matrix.org/latest/client-server-api/#room-events', 'notes': 'Practical thread model. Our isGroup ≈ room.join_rules; unreadCount ≈ unread_notifications.highlight_count.'}, {'source': 'Gmail API — Thread resource', 'url': 'https://developers.google.com/gmail/api/reference/rest/v1/users.threads', 'notes': 'Our messageCount ≈ messages.length; unreadCount derived from UNREAD labels on Thread messages.'}]},
    'conversion': {'name': 'conversion', 'plural': 'conversions', 'description': 'A contextual unit conversion — one that is NOT intrinsic to the units', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'allDay', 'ty': 'boolean'}, {'name': 'currentUrl', 'ty': 'string'}, {'name': 'dateUpdated', 'ty': 'datetime'}, {'name': 'distinctId', 'ty': 'string'}, {'name': 'endDate', 'ty': 'datetime'}, {'name': 'factor', 'ty': 'number'}, {'name': 'icalUid', 'ty': 'string'}, {'name': 'kind', 'ty': 'string'}, {'name': 'properties', 'ty': 'json'}, {'name': 'rate', 'ty': 'number'}, {'name': 'recurrence', 'ty': 'stringlist'}, {'name': 'showAs', 'ty': 'string'}, {'name': 'sourceTitle', 'ty': 'string'}, {'name': 'sourceUrl', 'ty': 'url'}, {'name': 'startDate', 'ty': 'datetime'}, {'name': 'status', 'ty': 'string'}, {'name': 'timezone', 'ty': 'string'}, {'name': 'visibility', 'ty': 'string'}], 'also': ['event'], 'display': {'subtitle': 'kind', 'highlights': ['startDate', 'endDate', 'location']}, 'prior_art': [{'source': 'NIH/NLM — UCUM conversion service', 'url': 'https://ucum.nlm.nih.gov/ucum-service.html', 'notes': 'The NIH service requires a MOLWEIGHT parameter to convert between molar and mass concentration — direct proof that the conversion is not intrinsic to the unit pair but depends on the substance.'}, {'source': 'QUDT — currency units carry no conversionMultiplier', 'url': 'https://qudt.org/doc/2024/12/DOC_VOCAB-UNITS-CURRENCY.html', 'notes': 'QUDT explicitly notes that FX rates are external data not encoded in QUDT — the same reason fx conversions are their own node here rather than a property of the currency unit.'}, {'source': 'ISO 4217 — Currency codes', 'url': 'https://www.iso.org/iso-4217-currency-codes.html', 'notes': 'Currency identity for the from/to units of an fx conversion.'}]},
    'creative_work': {'name': 'creative_work', 'plural': 'creative_works', 'description': "A creative work — the abstract level of FRBR's Work tier. Anything", 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'copyrightYear', 'ty': 'integer'}, {'name': 'coverage', 'ty': 'string'}, {'name': 'dateCreated', 'ty': 'date'}, {'name': 'description', 'ty': 'string'}, {'name': 'language', 'ty': 'string'}, {'name': 'license', 'ty': 'string'}, {'name': 'tags', 'ty': 'stringlist'}], 'display': {'subtitle': 'written_by', 'image': 'image', 'body': 'description', 'highlights': ['datePublished', 'published_by']}, 'prior_art': [{'source': 'schema.org/CreativeWork', 'url': 'https://schema.org/CreativeWork', 'notes': 'Our name=name; written_by≈author; published_by≈publisher; datePublished=datePublished; license=license; copyrightHolder= copyrightHolder; copyrightYear=copyrightYear; description= description; url=url; language=inLanguage; tags=keywords.'}, {'source': 'Dublin Core Metadata Element Set (ISO 15836)', 'url': 'https://www.dublincore.org/specifications/dublin-core/dces/', 'notes': 'Maps cleanly to all 15 DC elements except `type` (carried by the shape discriminator), `format` (subtype-specific), `identifier` (universal node id), `relation` (graph links), `subject` (tags).'}, {'source': 'FRBR (IFLA, 1998)', 'url': 'https://www.ifla.org/files/assets/cataloguing/frbr/frbr.pdf', 'notes': "creative_work corresponds to FRBR's Work tier (the abstract intellectual creation). Expression / Manifestation / Item not modeled in v1; subtype shapes carry equivalents as array fields (font.weights, font.formats)."}]},
    'credential': {'name': 'credential', 'plural': 'credentials', 'description': 'A credential held by AgentOS — the graph descriptor that mirrors one', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'domain', 'ty': 'string', 'required': True}, {'name': 'identifier', 'ty': 'string', 'required': True}, {'name': 'itemType', 'ty': 'string', 'required': True}, {'name': 'lastVerified', 'ty': 'datetime'}, {'name': 'obtainedAt', 'ty': 'datetime'}, {'name': 'refreshable', 'ty': 'boolean'}, {'name': 'source', 'ty': 'string'}, {'name': 'storeRowId', 'ty': 'integer'}], 'identity': ['domain', 'identifier', 'itemType'], 'display': {'subtitle': 'source'}, 'prior_art': [{'source': 'OAuth 2.0 Token Introspection (RFC 7662)', 'url': 'https://datatracker.ietf.org/doc/html/rfc7662', 'notes': 'RFC 7662 describes token metadata as a separate addressable resource from the token itself (active, exp, iss, sub, scope). Same split here: descriptor is queryable graph metadata, encrypted value is retrieved by a separate call (`auth_store.read` by identifier). Our obtainedAt/expiresAt/lastVerified mirror iat/exp/auth_time.'}, {'source': 'FIDO Metadata Service (MDS3)', 'url': 'https://fidoalliance.org/metadata/', 'notes': 'FIDO separates authenticator metadata from the authenticator itself — metadata is queryable, the cryptographic material is not. Mirrors our descriptor/vault split.'}, {'source': 'macOS Keychain SecItem attributes', 'url': 'https://developer.apple.com/documentation/security/keychain_services/keychain_items/item_attribute_keys_and_values', 'notes': 'Keychain separates `kSecAttr*` (metadata — server, account, creation/modification dates) from `kSecValueData` (the secret). Attributes are queryable without decrypting the value. Our fields map: kSecAttrServer → domain, kSecAttrAccount → identifier, kSecAttrCreationDate → obtainedAt, kSecAttrModificationDate → lastVerified.'}, {'source': 'schema.org/DigitalDocument (WebAuthn credentials stored as)', 'url': 'https://schema.org/DigitalDocument', 'notes': 'Weak alignment — schema.org has no native credential type. Cited only to note that existing web ontologies deliberately stop short of secret material; descriptor-only is the established pattern.'}]},
    'cursor': {'name': 'cursor', 'plural': 'cursors', 'description': 'A mouse-pointer image — the arrow, the I-beam, the hand, the resize', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'copyrightYear', 'ty': 'integer'}, {'name': 'coverage', 'ty': 'string'}, {'name': 'dateCreated', 'ty': 'date'}, {'name': 'description', 'ty': 'string'}, {'name': 'dimension', 'ty': 'integer'}, {'name': 'encoding', 'ty': 'string'}, {'name': 'filename', 'ty': 'string'}, {'name': 'format', 'ty': 'string'}, {'name': 'hotspotX', 'ty': 'integer'}, {'name': 'hotspotY', 'ty': 'integer'}, {'name': 'kind', 'ty': 'string'}, {'name': 'language', 'ty': 'string'}, {'name': 'license', 'ty': 'string'}, {'name': 'lineCount', 'ty': 'integer'}, {'name': 'mimeType', 'ty': 'string'}, {'name': 'path', 'ty': 'string'}, {'name': 'purpose', 'ty': 'string'}, {'name': 'sha', 'ty': 'string'}, {'name': 'size', 'ty': 'integer'}, {'name': 'tags', 'ty': 'stringlist'}], 'also': ['creative_work', 'file'], 'identity_any': ['sha', 'url'], 'display': {'subtitle': 'purpose', 'image': 'image', 'body': 'description', 'highlights': ['datePublished', 'published_by']}, 'prior_art': [{'source': 'CSS UI `cursor` property', 'url': 'https://www.w3.org/TR/css-ui-4/#cursor', 'notes': 'The render contract: `cursor: url(<url>) <hotspotX> <hotspotY>, <keyword>`. Our hotspotX/hotspotY ARE the `<x> <y>` the spec needs for image cursors; purpose maps to the trailing keyword.'}, {'source': 'Windows .cur / .ani cursor format', 'url': 'https://learn.microsoft.com/en-us/windows/win32/menurc/about-cursors', 'notes': "Source format of the bundled XP scheme — the .cur header carries the hotspot in its image-directory entry (bytes 4–7), which we read and record as hotspotX/hotspotY when downscaling to PNG. `.ani` (animated) is excluded — browsers don't support it in CSS cursor."}, {'source': 'schema.org/ImageObject', 'url': 'https://schema.org/ImageObject', 'notes': 'A cursor is an image artifact; most metadata (author, license, datePublished) comes from creative_work via `also`, dimension ≈ width/height.'}]},
    'dimension': {'name': 'dimension', 'plural': 'dimensions', 'description': 'A physical dimension — the abstract nature of a quantity, expressed as', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'amount', 'ty': 'integer'}, {'name': 'current', 'ty': 'integer'}, {'name': 'dimensionless', 'ty': 'boolean'}, {'name': 'key', 'ty': 'string', 'required': True}, {'name': 'label', 'ty': 'string'}, {'name': 'length', 'ty': 'integer'}, {'name': 'luminous', 'ty': 'integer'}, {'name': 'mass', 'ty': 'integer'}, {'name': 'temperature', 'ty': 'integer'}, {'name': 'time', 'ty': 'integer'}], 'identity': ['key'], 'display': {'subtitle': 'label'}, 'prior_art': [{'source': 'BIPM — SI Brochure, 9th edition (2019)', 'url': 'https://www.bipm.org/documents/20126/41483022/SI-Brochure-9-EN.pdf', 'notes': 'Defines the 7 base quantities (length, mass, time, electric current, thermodynamic temperature, amount of substance, luminous intensity) and their dimensions L, M, T, I, Θ, N, J. The seven exponent fields here are exactly those base dimensions.'}, {'source': 'ISO 80000-1 — Quantities and units, Part 1: General', 'url': 'https://www.iso.org/standard/76921.html', 'notes': 'The ISQ (International System of Quantities) — the rigorous definition of a quantity dimension as a product of base-quantity powers. This shape is a direct encoding of an ISQ dimension.'}, {'source': 'QUDT — QuantityKindDimensionVector', 'url': 'https://www.qudt.org/doc/DOC_SCHEMA-QUDT.html', 'notes': 'QUDT encodes the same 7 exponents as separate properties (qudt:dimensionExponentForMass etc.) plus a compact vector IRI. Our `key` mirrors that compact form; the seven integer fields mirror the per-dimension properties.'}]},
    'dns_record': {'name': 'dns_record', 'plural': 'dns_records', 'description': 'A DNS record for a domain. One domain has many records (A, CNAME, MX, TXT, etc.).', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'domain', 'ty': 'string', 'required': True}, {'name': 'priority', 'ty': 'integer'}, {'name': 'recordId', 'ty': 'string'}, {'name': 'recordName', 'ty': 'string', 'required': True}, {'name': 'recordType', 'ty': 'string', 'required': True}, {'name': 'ttl', 'ty': 'integer'}, {'name': 'type', 'ty': 'string'}, {'name': 'values', 'ty': 'stringlist'}], 'identity': ['domain', 'recordType', 'recordName'], 'display': {'subtitle': 'recordType'}, 'prior_art': [{'source': 'RFC 1035 (DNS)', 'url': 'https://datatracker.ietf.org/doc/html/rfc1035', 'notes': 'Foundational spec. Our domain/recordName/recordType/ttl/values map directly to NAME/TYPE/CLASS/TTL/RDATA.'}, {'source': 'RFC 7208 (SPF), RFC 6376 (DKIM), RFC 7489 (DMARC)', 'url': 'https://datatracker.ietf.org/doc/html/rfc7208', 'notes': 'TXT-record vocabularies that frequently populate our values[] for SPF, DKIM, and DMARC policy records.'}]},
    'document': {'name': 'document', 'plural': 'documents', 'description': 'A document — any human-readable text content with structure and authorship.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'abstract', 'ty': 'text'}, {'name': 'contentType', 'ty': 'string'}, {'name': 'encoding', 'ty': 'string'}, {'name': 'filename', 'ty': 'string'}, {'name': 'format', 'ty': 'string'}, {'name': 'kind', 'ty': 'string'}, {'name': 'language', 'ty': 'string'}, {'name': 'lineCount', 'ty': 'integer'}, {'name': 'mimeType', 'ty': 'string'}, {'name': 'path', 'ty': 'string'}, {'name': 'sha', 'ty': 'string'}, {'name': 'size', 'ty': 'integer'}, {'name': 'tableOfContents', 'ty': 'text'}, {'name': 'wordCount', 'ty': 'integer'}], 'also': ['file'], 'display': {'subtitle': 'contentType', 'body': 'abstract', 'highlights': ['datePublished', 'author', 'wordCount']}, 'prior_art': [{'source': 'Dublin Core Metadata Initiative', 'url': 'https://www.dublincore.org/specifications/dublin-core/dces/', 'notes': 'Our contentType ≈ dc:format; language = dc:language; author = dc:creator; references/citedBy ≈ dc:relation.'}, {'source': 'schema.org/DigitalDocument', 'url': 'https://schema.org/DigitalDocument', 'notes': 'Our abstract ≈ abstract; tableOfContents = hasPart or accessModeSufficient; wordCount = wordCount.'}, {'source': 'W3C Web Annotation Data Model', 'url': 'https://www.w3.org/TR/annotation-model/', 'notes': 'Our references[]/citedBy[] are annotation target/body relationships between documents.'}]},
    'domain': {'name': 'domain', 'plural': 'domains', 'description': 'A registered domain name. Also auto-created from email sender/recipient addresses.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'autoRenew', 'ty': 'boolean'}, {'name': 'nameservers', 'ty': 'stringlist'}, {'name': 'registrar', 'ty': 'string'}, {'name': 'status', 'ty': 'string'}], 'identity': ['name'], 'display': {'subtitle': 'registrar'}, 'prior_art': [{'source': 'RFC 1035 (Domain Names)', 'url': 'https://datatracker.ietf.org/doc/html/rfc1035', 'notes': 'Canonical domain-name syntax + nameservers + TTL. Our nameservers are NS records for the apex.'}, {'source': 'RFC 3912 (WHOIS)', 'url': 'https://datatracker.ietf.org/doc/html/rfc3912', 'notes': 'Our registrar/status/expiresAt/autoRenew come from WHOIS response fields.'}]},
    'email': {'name': 'email', 'plural': 'emails', 'description': 'An email message. Emails are also messages — querying by "message"', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'accountEmail', 'ty': 'string'}, {'name': 'attachments', 'ty': 'json'}, {'name': 'authResults', 'ty': 'string'}, {'name': 'bccRaw', 'ty': 'string'}, {'name': 'ccRaw', 'ty': 'string'}, {'name': 'conversationId', 'ty': 'string'}, {'name': 'deliveredTo', 'ty': 'string'}, {'name': 'draftId', 'ty': 'string'}, {'name': 'hasAttachments', 'ty': 'boolean'}, {'name': 'inReplyTo', 'ty': 'string'}, {'name': 'isAutomated', 'ty': 'boolean'}, {'name': 'isDraft', 'ty': 'boolean'}, {'name': 'isOutgoing', 'ty': 'boolean'}, {'name': 'isSent', 'ty': 'boolean'}, {'name': 'isSpam', 'ty': 'boolean'}, {'name': 'isStarred', 'ty': 'boolean'}, {'name': 'isTrash', 'ty': 'boolean'}, {'name': 'isUnread', 'ty': 'boolean'}, {'name': 'listId', 'ty': 'string'}, {'name': 'mailer', 'ty': 'string'}, {'name': 'manageSubscription', 'ty': 'string'}, {'name': 'messageId', 'ty': 'string'}, {'name': 'precedence', 'ty': 'string'}, {'name': 'references', 'ty': 'string'}, {'name': 'replyTo', 'ty': 'string'}, {'name': 'returnPath', 'ty': 'string'}, {'name': 'sizeEstimate', 'ty': 'integer'}, {'name': 'subject', 'ty': 'string'}, {'name': 'toRaw', 'ty': 'string'}, {'name': 'unsubscribe', 'ty': 'string'}, {'name': 'unsubscribeOneClick', 'ty': 'boolean'}], 'also': ['message'], 'identity': ['at', 'id'], 'display': {'subtitle': 'author'}, 'prior_art': [{'source': 'RFC 5322 (Internet Message Format)', 'url': 'https://datatracker.ietf.org/doc/html/rfc5322', 'notes': 'Supersedes RFC 2822. Our messageId/inReplyTo/references/replyTo map directly to Message-ID/In-Reply-To/References/Reply-To headers; toRaw/ccRaw/bccRaw are the literal header values.'}, {'source': 'RFC 2369 + RFC 8058 (List headers, one-click unsubscribe)', 'url': 'https://datatracker.ietf.org/doc/html/rfc2369', 'notes': 'Our unsubscribe/unsubscribeOneClick/listId are List-Unsubscribe/List-Unsubscribe-Post/List-ID. RFC 8058 defines the one-click POST semantics.'}, {'source': 'Gmail API Message resource', 'url': 'https://developers.google.com/gmail/api/reference/rest/v1/users.messages', 'notes': "Practical API mirror. Our sizeEstimate and isUnread/isStarred/isDraft/isSent/isTrash/isSpam correspond to Gmail's sizeEstimate and labelIds (UNREAD, STARRED, DRAFT, SENT, TRASH, SPAM)."}]},
    'episode': {'name': 'episode', 'plural': 'episodes', 'description': 'A single episode of a podcast or show. Transcribable.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'durationMs', 'ty': 'integer'}, {'name': 'episodeNumber', 'ty': 'integer'}, {'name': 'seasonNumber', 'ty': 'integer'}], 'display': {'subtitle': 'author'}, 'prior_art': [{'source': 'Apple Podcasts RSS Extensions (itunes:episode)', 'url': 'https://help.apple.com/itc/podcasts_connect/#/itcb54353390', 'notes': 'De-facto podcast metadata standard. Our episodeNumber/seasonNumber/ durationMs = itunes:episode/itunes:season/itunes:duration.'}, {'source': 'schema.org/PodcastEpisode', 'url': 'https://schema.org/PodcastEpisode', 'notes': 'Our series ≈ partOfSeries (PodcastSeries); transcribe ≈ transcript; guest ≈ actor.'}, {'source': 'Podcast Namespace (podcast:*)', 'url': 'https://podcastindex.org/namespace/1.0', 'notes': 'Modern open extension to RSS. Covers our guest, season, episode, and transcript relations via podcast:person, podcast:season, etc.'}]},
    'event': {'name': 'event', 'plural': 'events', 'description': 'Something that happens — at a time, optionally at a place, involving people.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'allDay', 'ty': 'boolean'}, {'name': 'currentUrl', 'ty': 'string'}, {'name': 'dateUpdated', 'ty': 'datetime'}, {'name': 'distinctId', 'ty': 'string'}, {'name': 'endDate', 'ty': 'datetime'}, {'name': 'icalUid', 'ty': 'string'}, {'name': 'properties', 'ty': 'json'}, {'name': 'recurrence', 'ty': 'stringlist'}, {'name': 'showAs', 'ty': 'string'}, {'name': 'sourceTitle', 'ty': 'string'}, {'name': 'sourceUrl', 'ty': 'url'}, {'name': 'startDate', 'ty': 'datetime'}, {'name': 'status', 'ty': 'string'}, {'name': 'timezone', 'ty': 'string'}, {'name': 'visibility', 'ty': 'string'}], 'identity': ['at', 'id'], 'display': {'subtitle': 'startDate', 'highlights': ['startDate', 'endDate', 'location']}, 'prior_art': [{'source': 'schema.org/Event', 'url': 'https://schema.org/Event', 'notes': "Core event type. Our startDate/endDate map 1:1; eventType is free-form vs. schema.org's subtype hierarchy (Concert, Conference, BusinessEvent). organizer/location match directly."}, {'source': 'RFC 5545 (iCalendar) VEVENT', 'url': 'https://datatracker.ietf.org/doc/html/rfc5545', 'notes': 'Our icalUid is their UID; recurrence is their RRULE; status maps to STATUS (TENTATIVE/CONFIRMED/CANCELLED); showAs ≈ TRANSP; involves[] ≈ ATTENDEE.'}, {'source': 'ActivityStreams 2.0 Event', 'url': 'https://www.w3.org/TR/activitystreams-vocabulary/#dfn-event', 'notes': 'Fediverse inbox format. Thinner than iCal — no native recurrence or showAs; our involves[] ≈ attendees via as:Relationship.'}]},
    'fare': {'name': 'fare', 'plural': 'fares', 'description': 'The priced class-of-service unit for a transport journey — the BASE', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'basePrice', 'ty': 'number'}, {'name': 'bookingCode', 'ty': 'string'}, {'name': 'changeable', 'ty': 'boolean'}, {'name': 'class', 'ty': 'string'}, {'name': 'components', 'ty': 'integer'}, {'name': 'conditions', 'ty': 'json'}, {'name': 'currency', 'ty': 'string'}, {'name': 'fareFamily', 'ty': 'string'}, {'name': 'identifier', 'ty': 'string', 'required': True}, {'name': 'milesEarned', 'ty': 'integer'}, {'name': 'passengerType', 'ty': 'string'}, {'name': 'pointsEarned', 'ty': 'integer'}, {'name': 'productType', 'ty': 'string'}, {'name': 'refundable', 'ty': 'boolean'}, {'name': 'restrictions', 'ty': 'stringlist'}], 'identity': ['at', 'identifier'], 'display': {'subtitle': 'fareFamily'}, 'prior_art': [{'source': 'IATA Fare Basis Code / ATPCO filings', 'url': 'https://en.wikipedia.org/wiki/Fare_basis_code', 'notes': "Airline canonical. First char = RBD/booking class (our `bookingCode`); remainder = airline-proprietary pointer into ATPCO-filed fare rules (our `identifier` as opaque string, `conditions` for the rule blob). Codes are 3-8 chars; we don't parse beyond the first char."}, {'source': 'IATA NDC FareDetail / FareComponent', 'url': 'https://developer.iata.org/en/ndc/', 'notes': "NDC's FareDetail.FareComponent carries FareBasis.FareBasisCode, FareBasis.RBD, Price.BaseAmount, FareRules.Penalty, and CabinType.CabinTypeCode. Our identifier/bookingCode/basePrice/ class/refundable map directly."}, {'source': 'Duffel Offer Slice / fare_basis_code', 'url': 'https://duffel.com/docs/api/v2/offers', 'notes': "Duffel surfaces fare_basis_code on each slice's segments along with cabin_class, cabin_class_marketing_name (our fareFamily), and passenger-level base_amount. Our basePrice = base_amount; class = cabin_class; fareFamily = cabin_class_marketing_name."}, {'source': 'Amtrak / Rail Europe fare types', 'url': 'https://www.amtrak.com/routes/fares', 'notes': 'Non-airline generalization. Amtrak fares are Saver / Value / Flexible / Premium / Business / First / Acela First / Acela First Refundable — their tier codes fit `identifier`; their names fit `fareFamily`; their rules fit `refundable`/ `changeable`/`restrictions`.'}, {'source': 'GTFS fare_products.txt (transit)', 'url': 'https://gtfs.org/documentation/schedule/reference/#fare_productstxt', 'notes': 'Open transit standard for fare products. Their fare_product_id = our identifier; fare_product_name = fareFamily; amount = basePrice; currency_code = currency. rider_category matches passengerType (adult/child/senior/student).'}, {'source': 'schema.org/Offer price + FlightReservation', 'url': 'https://schema.org/FlightReservation', 'notes': "schema.org's Offer.price + Offer.priceCurrency align with our basePrice + currency. schema.org has no fare-basis concept; NDC and GTFS fill that gap."}]},
    'file': {'name': 'file', 'plural': 'files', 'description': 'A file — source code, attachment, download, or any discrete digital artifact.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'encoding', 'ty': 'string'}, {'name': 'filename', 'ty': 'string'}, {'name': 'format', 'ty': 'string'}, {'name': 'kind', 'ty': 'string'}, {'name': 'lineCount', 'ty': 'integer'}, {'name': 'mimeType', 'ty': 'string'}, {'name': 'path', 'ty': 'string'}, {'name': 'sha', 'ty': 'string'}, {'name': 'size', 'ty': 'integer'}], 'identity_any': ['sha', 'url'], 'display': {'subtitle': 'path'}, 'prior_art': [{'source': 'IANA Media Types (RFC 6838)', 'url': 'https://datatracker.ietf.org/doc/html/rfc6838', 'notes': 'Our mimeType follows type/subtype syntax (text/plain, application/pdf). Canonical source for format identification.'}, {'source': 'schema.org/DigitalDocument', 'url': 'https://schema.org/DigitalDocument', 'notes': 'Our filename ≈ name; size ≈ contentSize; mimeType ≈ encodingFormat.'}, {'source': 'Git Internals (blob objects)', 'url': 'https://git-scm.com/book/en/v2/Git-Internals-Git-Objects', 'notes': "Our sha is a Git blob SHA-1 (40-hex). Git's content-addressable model underlies our repo-file identity."}]},
    'financial_account': {'name': 'financial_account', 'plural': 'financial_accounts', 'description': 'A financial account — bank checking/savings, brokerage, crypto wallet, etc.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'accountId', 'ty': 'string'}, {'name': 'accountNumber', 'ty': 'string'}, {'name': 'accountType', 'ty': 'string'}, {'name': 'available', 'ty': 'number'}, {'name': 'balance', 'ty': 'number'}, {'name': 'cardType', 'ty': 'string'}, {'name': 'creditLimit', 'ty': 'number'}, {'name': 'currency', 'ty': 'string'}, {'name': 'identifier', 'ty': 'string', 'required': True}, {'name': 'interestRate', 'ty': 'number'}, {'name': 'last4', 'ty': 'string'}, {'name': 'minimumPayment', 'ty': 'number'}, {'name': 'routingNumber', 'ty': 'string'}], 'identity': ['at', 'identifier'], 'display': {'subtitle': 'last4'}, 'prior_art': [{'source': 'OFX (Open Financial Exchange)', 'url': 'https://financialdataexchange.org/ofx', 'notes': 'Bank-feed canonical. Our accountNumber / routingNumber / balance / available map to OFX BANKACCTFROM / LEDGERBAL / AVAILBAL.'}, {'source': 'ISO 20022 Financial Messaging', 'url': 'https://www.iso20022.org/', 'notes': 'Modern bank-messaging standard. Our last4 / cardType / creditLimit / interestRate align with ISO 20022 Card / Account components.'}, {'source': 'schema.org/BankAccount', 'url': 'https://schema.org/BankAccount', 'notes': 'Our accountNumber ≈ accountId; balance / available are accountMinimumInflow / accountOverdraftLimit loosely; cardType fits schema.org/CreditCard.'}, {'source': '1Password Bank Account item', 'url': 'https://1password.com/', 'notes': "1P's Bank Account category holds institution + account number + routing + type — same shape. Their Crypto Wallet and Credit Card are separate categories; we treat them as different `accountType` values on the same shape for now, splitting only if the field diversity forces it."}]},
    'flight': {'name': 'flight', 'plural': 'flights', 'description': 'A flight — a specific leg of air travel. A flight IS a leg.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'allDay', 'ty': 'boolean'}, {'name': 'arrivalTime', 'ty': 'datetime'}, {'name': 'cabinClass', 'ty': 'string'}, {'name': 'carbonEmissions', 'ty': 'json'}, {'name': 'currentUrl', 'ty': 'string'}, {'name': 'dateUpdated', 'ty': 'datetime'}, {'name': 'departureTime', 'ty': 'datetime'}, {'name': 'distinctId', 'ty': 'string'}, {'name': 'duration', 'ty': 'string'}, {'name': 'durationMinutes', 'ty': 'integer'}, {'name': 'endDate', 'ty': 'datetime'}, {'name': 'flightNumber', 'ty': 'string'}, {'name': 'icalUid', 'ty': 'string'}, {'name': 'layoverMinutes', 'ty': 'integer'}, {'name': 'polyline', 'ty': 'string'}, {'name': 'properties', 'ty': 'json'}, {'name': 'recurrence', 'ty': 'stringlist'}, {'name': 'sequence', 'ty': 'integer'}, {'name': 'showAs', 'ty': 'string'}, {'name': 'sourceTitle', 'ty': 'string'}, {'name': 'sourceUrl', 'ty': 'url'}, {'name': 'startDate', 'ty': 'datetime'}, {'name': 'status', 'ty': 'string'}, {'name': 'stops', 'ty': 'integer'}, {'name': 'timezone', 'ty': 'string'}, {'name': 'trace', 'ty': 'json'}, {'name': 'tracePointCount', 'ty': 'integer'}, {'name': 'vehicleType', 'ty': 'string'}, {'name': 'visibility', 'ty': 'string'}], 'also': ['leg'], 'display': {'subtitle': 'airline', 'highlights': ['startDate', 'endDate', 'location']}, 'prior_art': [{'source': 'IATA Resolution 753 / Flight Codeshare', 'url': 'https://www.iata.org/en/programs/ops-infra/baggage/baggage-tracking/', 'notes': 'Our flightNumber follows IATA carrier-code + digits format (UA 1234). Canonical for cross-carrier flight identity.'}, {'source': 'Duffel / IATA NDC Slice+Segment', 'url': 'https://duffel.com/docs/api/v2/overview', 'notes': 'NDC models a trip (slice) as multiple flights (segments). Our flight shape = NDC segment; our trip = NDC slice.'}, {'source': 'schema.org/Flight', 'url': 'https://schema.org/Flight', 'notes': 'Our flightNumber = flightNumber; departsFrom/arrivesAt = departureAirport/arrivalAirport; departureTime/arrivalTime match directly; carbonEmissions ≈ estimatedFlightDuration + emissions extensions.'}]},
    'font': {'name': 'font', 'plural': 'fonts', 'description': 'A typeface — the family-level work. One node per font family', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'copyrightYear', 'ty': 'integer'}, {'name': 'coverage', 'ty': 'string'}, {'name': 'dateCreated', 'ty': 'date'}, {'name': 'description', 'ty': 'string'}, {'name': 'designerUrl', 'ty': 'string'}, {'name': 'family', 'ty': 'string'}, {'name': 'formats', 'ty': 'stringlist'}, {'name': 'genericFamily', 'ty': 'string'}, {'name': 'glyphCount', 'ty': 'integer'}, {'name': 'language', 'ty': 'string'}, {'name': 'license', 'ty': 'string'}, {'name': 'licenseInfoUrl', 'ty': 'string'}, {'name': 'postscriptName', 'ty': 'string'}, {'name': 'scripts', 'ty': 'stringlist'}, {'name': 'styles', 'ty': 'stringlist'}, {'name': 'tags', 'ty': 'stringlist'}, {'name': 'vendorUrl', 'ty': 'string'}, {'name': 'weights', 'ty': 'integerlist'}], 'also': ['creative_work'], 'identity_any': ['family', 'postscriptName'], 'display': {'subtitle': 'author', 'image': 'image', 'body': 'description', 'highlights': ['datePublished', 'published_by']}, 'prior_art': [{'source': 'schema.org/Typeface', 'url': 'https://schema.org/Typeface', 'notes': 'Schema.org added Typeface in 2024. Sparse compared to OpenType (fontFamily, format only) — we lean on the OpenType `name` table for most fields.'}, {'source': 'OpenType `name` table (ISO/IEC 14496-22)', 'url': 'https://learn.microsoft.com/en-us/typography/opentype/spec/name', 'notes': 'nameID 1=family; 6=postscriptName; 8=manufacturer (publisher in our model, via creative_work); 9=designer (author via creative_work); 13=licenseDescription (license via creative_work); 14=licenseInfoUrl; 11=vendorUrl; 12=designerUrl. Our font shape is a graph-native projection of this table; .woff2 metadata can round-trip losslessly.'}, {'source': 'Google Fonts metadata', 'url': 'https://fonts.google.com/specimen/Roboto', 'notes': 'Treats fonts as "families" with weights / styles arrays. Same model we adopt. Google Fonts also tracks subsets (Latin / Cyrillic / Greek) — equivalent to our scripts field.'}, {'source': 'ISO 15924 (script codes)', 'url': 'https://www.unicode.org/iso15924/iso15924-codes.html', 'notes': 'Our scripts field uses ISO 15924 four-letter codes (Latn / Cyrl / Grek / Arab / Hans / Hant / Jpan / Kore / etc.). Canonical identification of writing systems.'}]},
    'git_commit': {'name': 'git_commit', 'plural': 'git_commits', 'description': 'A git commit — a single point in version control history.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'additions', 'ty': 'integer'}, {'name': 'allDay', 'ty': 'boolean'}, {'name': 'committedAt', 'ty': 'datetime'}, {'name': 'currentUrl', 'ty': 'string'}, {'name': 'dateUpdated', 'ty': 'datetime'}, {'name': 'deletions', 'ty': 'integer'}, {'name': 'distinctId', 'ty': 'string'}, {'name': 'endDate', 'ty': 'datetime'}, {'name': 'filesChanged', 'ty': 'integer'}, {'name': 'icalUid', 'ty': 'string'}, {'name': 'message', 'ty': 'text'}, {'name': 'properties', 'ty': 'json'}, {'name': 'recurrence', 'ty': 'stringlist'}, {'name': 'sha', 'ty': 'string'}, {'name': 'shortHash', 'ty': 'string'}, {'name': 'showAs', 'ty': 'string'}, {'name': 'sourceTitle', 'ty': 'string'}, {'name': 'sourceUrl', 'ty': 'url'}, {'name': 'startDate', 'ty': 'datetime'}, {'name': 'status', 'ty': 'string'}, {'name': 'timezone', 'ty': 'string'}, {'name': 'visibility', 'ty': 'string'}], 'also': ['event'], 'display': {'subtitle': 'author', 'highlights': ['startDate', 'endDate', 'location']}, 'prior_art': [{'source': 'Git Internals — commit object', 'url': 'https://git-scm.com/book/en/v2/Git-Internals-Git-Objects', 'notes': "Our sha/shortHash/message/parent match the commit object exactly. author/committer follow Git's distinct author-vs-committer model."}, {'source': 'Conventional Commits 1.0', 'url': 'https://www.conventionalcommits.org/en/v1.0.0/', 'notes': "Practical structure for message field (type(scope): subject). Optional — we don't enforce but it's compatible."}]},
    'group': {'name': 'group', 'plural': 'groups', 'description': 'A group or community — online group, reading group, etc.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'category', 'ty': 'string'}, {'name': 'memberCount', 'ty': 'integer'}], 'identity': ['at', 'id'], 'display': {'subtitle': 'category'}, 'prior_art': [{'source': 'schema.org/Group (via Organization/memberOf)', 'url': 'https://schema.org/Organization', 'notes': 'schema.org models groups as Organization. Our memberCount ≈ numberOfEmployees loosely; category ≈ naics/knowsAbout.'}, {'source': 'FOAF Group', 'url': 'http://xmlns.com/foaf/spec/#term_Group', 'notes': 'Foundational social-graph vocabulary. foaf:member populates membership; category has no direct FOAF peer.'}]},
    'health-biomarker': {'name': 'health-biomarker', 'plural': 'health-biomarkers', 'description': 'The *definition* of a measurable health quantity — TSH, LDL cholesterol,', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'analyteType', 'ty': 'string'}, {'name': 'category', 'ty': 'string'}, {'name': 'description', 'ty': 'text'}, {'name': 'loincCode', 'ty': 'string'}, {'name': 'measure', 'ty': 'string'}], 'identity_any': ['loincCode', 'measure'], 'display': {'subtitle': 'category'}, 'prior_art': [{'source': 'HL7 FHIR R5 — ObservationDefinition', 'url': 'https://www.hl7.org/fhir/observationdefinition.html', 'notes': "FHIR's ObservationDefinition is the reusable definition of an observable, separate from the Observation that records a value. Our measure/category map to its code + quantitativeDetails. We deliberately do NOT include its qualifiedInterval — reference ranges are their own shape (health-reference-range)."}, {'source': 'LOINC — Logical Observation Identifiers Names and Codes', 'url': 'https://loinc.org/', 'notes': 'The universal code system for lab and clinical observations. loincCode is the join key — every lab observable has a LOINC code (TSH 3016-3, LDL 2089-1, HbA1c 4548-4). LOINC identifies the observable only; it carries no reference range.'}]},
    'health-condition': {'name': 'health-condition', 'plural': 'health-conditions', 'description': 'A health condition — a diagnosis, problem, symptom, or family-history', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'allDay', 'ty': 'boolean'}, {'name': 'bodySite', 'ty': 'string'}, {'name': 'clinicalArea', 'ty': 'string'}, {'name': 'clinicalStatus', 'ty': 'string'}, {'name': 'currentUrl', 'ty': 'string'}, {'name': 'dateUpdated', 'ty': 'datetime'}, {'name': 'distinctId', 'ty': 'string'}, {'name': 'endDate', 'ty': 'datetime'}, {'name': 'icalUid', 'ty': 'string'}, {'name': 'icd10Code', 'ty': 'string'}, {'name': 'mitigation', 'ty': 'text'}, {'name': 'properties', 'ty': 'json'}, {'name': 'proximity', 'ty': 'string'}, {'name': 'recurrence', 'ty': 'stringlist'}, {'name': 'severity', 'ty': 'string'}, {'name': 'showAs', 'ty': 'string'}, {'name': 'snomedCode', 'ty': 'string'}, {'name': 'sourceTitle', 'ty': 'string'}, {'name': 'sourceUrl', 'ty': 'url'}, {'name': 'startDate', 'ty': 'datetime'}, {'name': 'status', 'ty': 'string'}, {'name': 'timezone', 'ty': 'string'}, {'name': 'verificationStatus', 'ty': 'string'}, {'name': 'visibility', 'ty': 'string'}], 'also': ['event'], 'identity_any': ['snomedCode', 'name'], 'display': {'subtitle': 'clinicalStatus', 'highlights': ['startDate', 'endDate', 'location']}, 'prior_art': [{'source': 'HL7 FHIR R5 — Condition', 'url': 'https://www.hl7.org/fhir/condition.html', 'notes': "The resource for a problem/diagnosis. Our clinicalStatus, verificationStatus, severity, bodySite, onsetDate, abatementDate map directly. proximity='self' is a plain FHIR Condition."}, {'source': 'HL7 FHIR R5 — FamilyMemberHistory', 'url': 'https://www.hl7.org/fhir/familymemberhistory.html', 'notes': "FHIR's separate resource for hereditary risk. We fold it in via proximity — proximity='father'|'extended-family' makes a condition node a family-history entry. FamilyMemberHistory.condition ≈ this node; FamilyMemberHistory.relationship ≈ our proximity. Deliberate divergence from FHIR's two-resource split."}, {'source': 'SNOMED CT', 'url': 'https://www.snomed.org/', 'notes': 'The universal clinical terminology. snomedCode is the canonical identity (asthma 195967001, eczema 43116000). FHIR Condition.code is SNOMED-coded; this is the join key to the wider clinical world.'}, {'source': 'ICD-10-CM', 'url': 'https://www.cdc.gov/nchs/icd/icd-10-cm.htm', 'notes': 'The diagnosis/billing code system. icd10Code captures the code when it appears on an insurance claim or discharge summary — complements (does not replace) SNOMED.'}]},
    'health-immunization': {'name': 'health-immunization', 'plural': 'health-immunizations', 'description': 'An immunization — a single vaccine administration at a point in time.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'allDay', 'ty': 'boolean'}, {'name': 'currentUrl', 'ty': 'string'}, {'name': 'cvxCode', 'ty': 'string'}, {'name': 'dateAdministered', 'ty': 'datetime'}, {'name': 'dateUpdated', 'ty': 'datetime'}, {'name': 'diseaseTarget', 'ty': 'string'}, {'name': 'distinctId', 'ty': 'string'}, {'name': 'doseNumber', 'ty': 'integer'}, {'name': 'endDate', 'ty': 'datetime'}, {'name': 'icalUid', 'ty': 'string'}, {'name': 'lotNumber', 'ty': 'string'}, {'name': 'manufacturer', 'ty': 'string'}, {'name': 'notes', 'ty': 'text'}, {'name': 'properties', 'ty': 'json'}, {'name': 'recurrence', 'ty': 'stringlist'}, {'name': 'route', 'ty': 'string'}, {'name': 'seriesDoses', 'ty': 'integer'}, {'name': 'showAs', 'ty': 'string'}, {'name': 'site', 'ty': 'string'}, {'name': 'sourceTitle', 'ty': 'string'}, {'name': 'sourceUrl', 'ty': 'url'}, {'name': 'startDate', 'ty': 'datetime'}, {'name': 'status', 'ty': 'string'}, {'name': 'timezone', 'ty': 'string'}, {'name': 'visibility', 'ty': 'string'}], 'also': ['event'], 'display': {'subtitle': 'dateAdministered', 'highlights': ['startDate', 'endDate', 'location']}, 'prior_art': [{'source': 'HL7 FHIR R5 — Immunization', 'url': 'https://www.hl7.org/fhir/immunization.html', 'notes': 'The resource for an administered vaccine. dateAdministered ≈ occurrenceDateTime; manufacturer ≈ manufacturer; lotNumber ≈ lotNumber; site/route ≈ site/route; doseNumber ≈ protocolApplied.doseNumber; seriesDoses ≈ protocolApplied.seriesDoses.'}, {'source': 'CDC CVX — Vaccine Administered code set', 'url': 'https://www2a.cdc.gov/vaccines/iis/iisstandards/vaccines.asp?rpt=cvx', 'notes': 'The US standard vaccine code system. cvxCode is the canonical vaccine identity (CVX 208 = COVID-19 Pfizer, CVX 20 = DTaP). FHIR Immunization.vaccineCode is CVX-coded.'}, {'source': 'HL7 v2.x — VXU (Unsolicited Vaccination Update)', 'url': 'https://www.cdc.gov/vaccines/programs/iis/technical-guidance/hl7.html', 'notes': 'The message format Immunization Information Systems exchange. The RXA segment carries date, CVX, lot, manufacturer, site, route — confirms the field set.'}]},
    'health-lab': {'name': 'health-lab', 'plural': 'health-labs', 'description': 'A clinical laboratory or testing facility — the place that processes a', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'accreditation', 'ty': 'string'}, {'name': 'actorType', 'ty': 'string'}, {'name': 'ccn', 'ty': 'string'}, {'name': 'cliaNumber', 'ty': 'string'}, {'name': 'industry', 'ty': 'string'}, {'name': 'labType', 'ty': 'string'}, {'name': 'npi', 'ty': 'string'}], 'also': ['organization'], 'identity_any': ['cliaNumber', 'url'], 'display': {'subtitle': 'labType', 'image': 'image', 'highlights': ['headquarters']}, 'prior_art': [{'source': 'schema.org/MedicalOrganization / DiagnosticLab', 'url': 'https://schema.org/DiagnosticLab', 'notes': "schema.org's DiagnosticLab is a MedicalOrganization subtype, which is an Organization subtype — exactly our also:[organization] chain. Our labType refines what schema.org leaves implicit."}, {'source': 'CLIA — Clinical Laboratory Improvement Amendments', 'url': 'https://www.cms.gov/medicare/quality/clinical-laboratory-improvement-amendments', 'notes': 'cliaNumber, npi (the organizational/type-2 National Provider Identifier), and ccn (the Medicare CMS Certification Number) are all CMS-issued identifiers a US testing facility carries. cliaNumber is the canonical identity for a US clinical lab.'}, {'source': 'HL7 FHIR R5 — Organization (role: laboratory)', 'url': 'https://www.hl7.org/fhir/organization.html', 'notes': 'FHIR models a lab as an Organization with a laboratory role code, not a distinct resource — consistent with our also:[organization]. FHIR Observation.performer / DiagnosticReport.performer reference it; our health-panel.performedAt and health-reference-range. issuingLab links are the same linkage.'}]},
    'health-panel': {'name': 'health-panel', 'plural': 'health-panels', 'description': 'A panel — a named grouping of biomarkers ordered and reported together.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'allDay', 'ty': 'boolean'}, {'name': 'arrangement', 'ty': 'string'}, {'name': 'currentUrl', 'ty': 'string'}, {'name': 'dateUpdated', 'ty': 'datetime'}, {'name': 'default_view', 'ty': 'string'}, {'name': 'description', 'ty': 'text'}, {'name': 'distinctId', 'ty': 'string'}, {'name': 'endDate', 'ty': 'datetime'}, {'name': 'fasting', 'ty': 'boolean'}, {'name': 'icalUid', 'ty': 'string'}, {'name': 'icon_size', 'ty': 'integer'}, {'name': 'isDefault', 'ty': 'boolean'}, {'name': 'isPublic', 'ty': 'boolean'}, {'name': 'itemCount', 'ty': 'integer'}, {'name': 'listId', 'ty': 'string'}, {'name': 'listType', 'ty': 'string'}, {'name': 'member_shape', 'ty': 'string'}, {'name': 'ordering_mode', 'ty': 'string'}, {'name': 'panelCode', 'ty': 'string'}, {'name': 'path', 'ty': 'string'}, {'name': 'privacy', 'ty': 'string'}, {'name': 'properties', 'ty': 'json'}, {'name': 'recurrence', 'ty': 'stringlist'}, {'name': 'showAs', 'ty': 'string'}, {'name': 'sort_by', 'ty': 'string'}, {'name': 'sourceTitle', 'ty': 'string'}, {'name': 'sourceUrl', 'ty': 'url'}, {'name': 'startDate', 'ty': 'datetime'}, {'name': 'status', 'ty': 'string'}, {'name': 'timezone', 'ty': 'string'}, {'name': 'visibility', 'ty': 'string'}], 'also': ['list', 'event'], 'display': {'subtitle': 'startDate', 'highlights': ['startDate', 'endDate', 'location']}, 'prior_art': [{'source': 'HL7 FHIR R5 — DiagnosticReport', 'url': 'https://www.hl7.org/fhir/diagnosticreport.html', 'notes': 'A dated panel is a DiagnosticReport: a set of observations grouped under one report with an effective date and a performer. Our `contains` links (from `list`) ≈ DiagnosticReport.result; effectiveDate ≈ effectiveDateTime; performedAt ≈ performer.'}, {'source': 'LOINC — Panels and Forms', 'url': 'https://loinc.org/panels/', 'notes': 'LOINC defines panel codes and their member observables (CBC panel 58410-2 enumerates hemoglobin, hematocrit, WBC, …). panelCode plus the contains→biomarker links mirror a LOINC panel definition.'}, {'source': 'schema.org/MedicalTest', 'url': 'https://schema.org/MedicalTest', 'notes': 'Lighter-weight precedent — a diagnostic test with usedToDiagnose / normalRange. Our panel is the grouping; biomarkers and health-reference-range carry the observable detail and the ranges.'}]},
    'health-procedure': {'name': 'health-procedure', 'plural': 'health-procedures', 'description': 'A procedure — a clinical action performed on the body. Surgeries', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'allDay', 'ty': 'boolean'}, {'name': 'bodySite', 'ty': 'string'}, {'name': 'cptCode', 'ty': 'string'}, {'name': 'currentUrl', 'ty': 'string'}, {'name': 'dateUpdated', 'ty': 'datetime'}, {'name': 'distinctId', 'ty': 'string'}, {'name': 'endDate', 'ty': 'datetime'}, {'name': 'findings', 'ty': 'text'}, {'name': 'followUp', 'ty': 'text'}, {'name': 'icalUid', 'ty': 'string'}, {'name': 'outcome', 'ty': 'string'}, {'name': 'performedDate', 'ty': 'datetime'}, {'name': 'procedureType', 'ty': 'string'}, {'name': 'properties', 'ty': 'json'}, {'name': 'recurrence', 'ty': 'stringlist'}, {'name': 'showAs', 'ty': 'string'}, {'name': 'snomedCode', 'ty': 'string'}, {'name': 'sourceTitle', 'ty': 'string'}, {'name': 'sourceUrl', 'ty': 'url'}, {'name': 'startDate', 'ty': 'datetime'}, {'name': 'status', 'ty': 'string'}, {'name': 'timezone', 'ty': 'string'}, {'name': 'visibility', 'ty': 'string'}], 'also': ['event'], 'identity_any': ['cptCode', 'snomedCode', 'id'], 'display': {'subtitle': 'performedDate', 'highlights': ['startDate', 'endDate', 'location']}, 'prior_art': [{'source': 'HL7 FHIR R5 — Procedure', 'url': 'https://www.hl7.org/fhir/procedure.html', 'notes': 'The resource for an action performed on a patient. performedDate ≈ occurrenceDateTime/occurrencePeriod; status ≈ status; bodySite ≈ bodySite; outcome ≈ outcome; findings ≈ report + note; `treats` link ≈ reason; performer ≈ performer.actor. `orderedBy` ≈ basedOn → ServiceRequest.requester — the clinician who ordered the study, which on imaging/scopes is rarely the one who performs it.'}, {'source': 'CPT — Current Procedural Terminology (AMA)', 'url': 'https://www.ama-assn.org/practice-management/cpt', 'notes': 'The US procedure code system used for billing. cptCode is the identity on insurance claims and operative records (septoplasty 30520, colonoscopy 45378).'}, {'source': 'SNOMED CT — Procedure axis', 'url': 'https://www.snomed.org/', 'notes': "SNOMED's procedure hierarchy provides the clinical (non-billing) code. FHIR Procedure.code is SNOMED-coded; snomedCode is the join key to the clinical ontology."}]},
    'health-reference-range': {'name': 'health-reference-range', 'plural': 'health-reference-ranges', 'description': 'A lab-specific reference interval — the "normal range" for a biomarker,', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'ageHigh', 'ty': 'number'}, {'name': 'ageLow', 'ty': 'number'}, {'name': 'allDay', 'ty': 'boolean'}, {'name': 'category', 'ty': 'string'}, {'name': 'currentUrl', 'ty': 'string'}, {'name': 'dateUpdated', 'ty': 'datetime'}, {'name': 'distinctId', 'ty': 'string'}, {'name': 'endDate', 'ty': 'datetime'}, {'name': 'fasting', 'ty': 'boolean'}, {'name': 'gestationalAge', 'ty': 'string'}, {'name': 'high', 'ty': 'number'}, {'name': 'icalUid', 'ty': 'string'}, {'name': 'low', 'ty': 'number'}, {'name': 'method', 'ty': 'string', 'required': True}, {'name': 'pregnancy', 'ty': 'string'}, {'name': 'properties', 'ty': 'json'}, {'name': 'provenance', 'ty': 'string'}, {'name': 'recurrence', 'ty': 'stringlist'}, {'name': 'refText', 'ty': 'string'}, {'name': 'sex', 'ty': 'string'}, {'name': 'showAs', 'ty': 'string'}, {'name': 'sourceTitle', 'ty': 'string'}, {'name': 'sourceUrl', 'ty': 'url'}, {'name': 'startDate', 'ty': 'datetime', 'required': True}, {'name': 'status', 'ty': 'string'}, {'name': 'timeOfDay', 'ty': 'string'}, {'name': 'timezone', 'ty': 'string'}, {'name': 'unit', 'ty': 'string'}, {'name': 'visibility', 'ty': 'string'}], 'also': ['event'], 'identity': ['analyte', 'issuingLab', 'method', 'startDate'], 'display': {'subtitle': 'refText', 'highlights': ['startDate', 'endDate', 'location']}, 'prior_art': [{'source': 'CLSI EP28-A3c — Defining, Establishing, and Verifying Reference Intervals', 'url': 'https://clsi.org/shop/standards/ep28/', 'notes': 'The authoritative protocol. Each lab must establish (de novo, min n=120 per partition) or verify (min n=20) its own intervals. `provenance` (established/verified/manufacturer-claimed) comes directly from this guideline; it is why two same-instrument labs legitimately diverge.'}, {'source': 'HL7 FHIR R5 — ObservationDefinition.qualifiedInterval', 'url': 'https://www.hl7.org/fhir/observationdefinition.html', 'notes': 'The closest standard precedent — a reusable, multi-context interval. Our category maps to its rangeCategory; range to range; age/gestationalAge/sex to the same; condition ≈ our population fields. But qualifiedInterval has NO issuingLab and NO validity window — this shape adds both. qualifiedInterval is the lossy EXPORT projection of this shape, not its equal.'}, {'source': 'HL7 FHIR R5 — Observation.referenceRange', 'url': 'https://www.hl7.org/fhir/observation.html', 'notes': "FHIR's other reference-range model — inlined on the result as a denormalized snapshot (low/high/normalValue/type/appliesTo/age/ text). measure keeps that snapshot too (its refLow/refHigh fields); this shape is the normalized, reusable form the snapshot can point back to."}, {'source': 'OMOP CDM v5.4 — MEASUREMENT.range_low / range_high', 'url': 'https://ohdsi.github.io/CommonDataModel/cdm54.html', 'notes': 'OMOP inlines range_low/range_high as columns on the measurement row — "no separate standalone table for reference ranges." Confirms the gap: no major model makes the range first-class.'}]},
    'icon': {'name': 'icon', 'plural': 'icons', 'description': 'A small graphic intended for UI use — toolbar buttons, file-type', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'component', 'ty': 'string'}, {'name': 'copyrightYear', 'ty': 'integer'}, {'name': 'coverage', 'ty': 'string'}, {'name': 'dateCreated', 'ty': 'date'}, {'name': 'description', 'ty': 'string'}, {'name': 'dimension', 'ty': 'integer'}, {'name': 'format', 'ty': 'string'}, {'name': 'language', 'ty': 'string'}, {'name': 'license', 'ty': 'string'}, {'name': 'purpose', 'ty': 'string'}, {'name': 'style', 'ty': 'string'}, {'name': 'tags', 'ty': 'stringlist'}], 'also': ['creative_work'], 'identity_any': ['component', 'url'], 'display': {'subtitle': 'purpose', 'image': 'image', 'body': 'description', 'highlights': ['datePublished', 'published_by']}, 'prior_art': [{'source': 'schema.org/ImageObject', 'url': 'https://schema.org/ImageObject', 'notes': "Icons could be modeled as ImageObject — we chose a distinct shape because the role-specific `purpose` field has no counterpart on ImageObject (which is purpose-agnostic by design) and because component-backed icons aren't fetchable as image URLs."}, {'source': 'Iconify metadata', 'url': 'https://iconify.design/', 'notes': "Iconify treats icons as named entries within an icon set, each with a category and tags. Our `purpose` field plays the same role as Iconify's category; our `style` plays the same role as Iconify's iconset style attribute (filled / outline / pixel)."}, {'source': 'Material Symbols metadata', 'url': 'https://fonts.google.com/icons', 'notes': "Material Symbols ship as a variable icon font with `fill`, `weight`, `grade`, and `optical-size` axes. Our shape doesn't model variable axes (Material Symbols would be one font, not one icon-per-glyph) — we model icons that live OUTSIDE icon fonts."}, {'source': 'macOS / Windows system icon naming', 'url': 'https://learn.microsoft.com/en-us/windows/win32/uxguide/vis-icons', 'notes': 'Both platforms standardize on role-named icons (e.g. "back", "forward", "close") rather than file-named icons. Our `purpose` field follows the same convention; theme authors register icons by their semantic role, not by a filename slug.'}]},
    'image': {'name': 'image', 'plural': 'images', 'description': 'An image file. Photos, screenshots, diagrams, artwork.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'altText', 'ty': 'string'}, {'name': 'appName', 'ty': 'string'}, {'name': 'copyrightYear', 'ty': 'integer'}, {'name': 'coverage', 'ty': 'string'}, {'name': 'dateCreated', 'ty': 'date'}, {'name': 'description', 'ty': 'string'}, {'name': 'displayId', 'ty': 'integer'}, {'name': 'displayIndex', 'ty': 'integer'}, {'name': 'encoding', 'ty': 'string'}, {'name': 'filename', 'ty': 'string'}, {'name': 'format', 'ty': 'string'}, {'name': 'height', 'ty': 'integer'}, {'name': 'kind', 'ty': 'string'}, {'name': 'language', 'ty': 'string'}, {'name': 'license', 'ty': 'string'}, {'name': 'lineCount', 'ty': 'integer'}, {'name': 'mimeType', 'ty': 'string'}, {'name': 'path', 'ty': 'string'}, {'name': 'sha', 'ty': 'string'}, {'name': 'size', 'ty': 'integer'}, {'name': 'tags', 'ty': 'stringlist'}, {'name': 'width', 'ty': 'integer'}, {'name': 'windowId', 'ty': 'integer'}], 'also': ['creative_work', 'file'], 'identity_any': ['sha', 'url'], 'display': {'subtitle': 'format', 'image': 'image', 'body': 'description', 'highlights': ['datePublished', 'published_by']}, 'prior_art': [{'source': 'schema.org/ImageObject', 'url': 'https://schema.org/ImageObject', 'notes': 'Our width/height = width/height; format ≈ encodingFormat; altText = caption/accessibilityCaption.'}, {'source': 'IANA Media Types (image/*)', 'url': 'https://www.iana.org/assignments/media-types/media-types.xhtml#image', 'notes': 'Our format values (PNG, JPEG, WebP, SVG) align with registered image/* media types.'}, {'source': 'Exif 2.3 (JEITA CP-3451)', 'url': 'https://www.cipa.jp/std/documents/e/DC-008-Translation-2019-E.pdf', 'notes': 'Source of most image metadata fields. width/height come from Exif PixelXDimension/PixelYDimension.'}]},
    'insurance_coverage': {'name': 'insurance_coverage', 'plural': 'insurance_coverages', 'description': 'A single benefit line within an insurance policy — the unit at which a', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'coinsurance', 'ty': 'number'}, {'name': 'copay', 'ty': 'number'}, {'name': 'currency', 'ty': 'string'}, {'name': 'deductible', 'ty': 'number'}, {'name': 'limit', 'ty': 'number'}, {'name': 'limitBasis', 'ty': 'string'}, {'name': 'notes', 'ty': 'text'}, {'name': 'outOfPocketMax', 'ty': 'number'}, {'name': 'requiresPreauth', 'ty': 'boolean'}, {'name': 'requiresReferral', 'ty': 'boolean'}, {'name': 'waitingPeriodMonths', 'ty': 'number'}], 'display': {'subtitle': 'limit', 'highlights': ['limit', 'requiresPreauth', 'requiresReferral', 'deductible']}, 'prior_art': [{'source': 'HL7 FHIR R5 — InsurancePlan.coverage.benefit & Coverage.costToBeneficiary', 'url': 'https://www.hl7.org/fhir/insuranceplan-definitions.html#InsurancePlan.coverage.benefit', 'notes': "FHIR models a benefit with a type + a list of limits, and cost- sharing (copay/coinsurance/deductible) on Coverage.costToBeneficiary. Our limit/limitBasis ≈ benefit.limit{value,code}; copay/coinsurance/ deductible/outOfPocketMax ≈ costToBeneficiary value/type. FHIR's benefit.requirement (free-text access conditions) is split here into the queryable gates requiresPreauth / requiresReferral plus prose in notes — and the verbatim clause on the evidenced_by link."}, {'source': 'ACORD — Coverage / Limit / Deductible', 'url': 'https://www.acord.org/standards-architecture/reference-architecture', 'notes': "ACORD Coverage carries Limit (with a basis: per-occurrence, aggregate, per-person) and Deductible. Our limit + limitBasis + deductible map directly; this is the P&C side (auto, renters, umbrella) that FHIR's health framing doesn't cover."}, {'source': 'US Summary of Benefits and Coverage (SBC)', 'url': 'https://www.cms.gov/marketplace/about/oversight/other-insurance-protections/summary-benefits-coverage-sbc-resources', 'notes': 'The federally-standardized consumer benefit summary: deductible, out-of-pocket maximum, copay, coinsurance per service category. Our health-line field set mirrors the SBC columns.'}]},
    'insurance_policy': {'name': 'insurance_policy', 'plural': 'insurance_policies', 'description': 'A contract of indemnity — one party (the insured) pays premiums to a', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'allDay', 'ty': 'boolean'}, {'name': 'autoRenew', 'ty': 'boolean'}, {'name': 'billingType', 'ty': 'string'}, {'name': 'coverageType', 'ty': 'string'}, {'name': 'currency', 'ty': 'string'}, {'name': 'currentUrl', 'ty': 'string'}, {'name': 'dateUpdated', 'ty': 'datetime'}, {'name': 'distinctId', 'ty': 'string'}, {'name': 'endDate', 'ty': 'datetime'}, {'name': 'groupNumber', 'ty': 'string'}, {'name': 'guestPassQuantity', 'ty': 'integer'}, {'name': 'icalUid', 'ty': 'string'}, {'name': 'memberId', 'ty': 'string'}, {'name': 'network', 'ty': 'string'}, {'name': 'policyNumber', 'ty': 'string', 'required': True}, {'name': 'price', 'ty': 'number'}, {'name': 'properties', 'ty': 'json'}, {'name': 'recurrence', 'ty': 'stringlist'}, {'name': 'showAs', 'ty': 'string'}, {'name': 'sourceTitle', 'ty': 'string'}, {'name': 'sourceUrl', 'ty': 'url'}, {'name': 'startDate', 'ty': 'datetime'}, {'name': 'status', 'ty': 'string'}, {'name': 'tier', 'ty': 'string'}, {'name': 'timezone', 'ty': 'string'}, {'name': 'useCount', 'ty': 'integer'}, {'name': 'visibility', 'ty': 'string'}], 'also': ['membership'], 'identity': ['underwritten_by', 'policyNumber'], 'display': {'subtitle': 'coverageType', 'highlights': ['coverageType', 'memberId', 'network', 'policyNumber']}, 'prior_art': [{'source': 'HL7 FHIR R5 — Coverage', 'url': 'https://www.hl7.org/fhir/coverage.html', 'notes': 'The canonical health-insurance enrollment resource. Our memberId ≈ Coverage.subscriberId / Coverage.beneficiary; groupNumber ≈ Coverage.class[type=group]; underwritten_by ≈ Coverage.payor; under (plan) ≈ Coverage.class[type=plan]; network ≈ Coverage.network. Coverage.period maps to our inherited event.startDate / endDate.'}, {'source': 'HL7 FHIR R5 — InsurancePlan', 'url': 'https://www.hl7.org/fhir/insuranceplan.html', 'notes': "Describes the PLAN (the product), distinct from a person's Coverage. We split the same way — the plan is a `product` reached via `under`; InsurancePlan.coverage[].benefit (limits, cost-sharing) is our `insurance_coverage` nodes reached via `provides`."}, {'source': 'ACORD Reference Architecture — Policy / Coverage / Producer', 'url': 'https://www.acord.org/standards-architecture/reference-architecture', 'notes': 'The P&C industry data standard. ACORD separates Insurer (carrier), Producer (agent/broker who sells), and Policy → Coverage → Limit / Deductible. Our underwritten_by ≈ Insurer, sold_by ≈ Producer, and insurance_coverage ≈ ACORD Coverage with its Limit/Deductible.'}, {'source': 'schema.org/ProgramMembership & schema.org/Permit', 'url': 'https://schema.org/ProgramMembership', 'notes': 'schema.org has no first-class insurance policy type; the closest framing is a membership/permit granted by an organization for a period — which is exactly why we model the policy as `also: [membership]` rather than inventing a parallel lifecycle.'}]},
    'intellectual_property': {'name': 'intellectual_property', 'plural': 'intellectual_properties', 'description': 'A registered or pending intellectual-property right — a trademark,', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'category', 'ty': 'string'}, {'name': 'filingBasis', 'ty': 'string'}, {'name': 'identifier', 'ty': 'string'}, {'name': 'mark', 'ty': 'string'}, {'name': 'niceClass', 'ty': 'integerlist'}, {'name': 'register', 'ty': 'string'}, {'name': 'renewalPeriod', 'ty': 'string'}, {'name': 'status', 'ty': 'string'}, {'name': 'validIn', 'ty': 'string'}, {'name': 'verificationUrl', 'ty': 'url'}], 'identity_any': ['identifier'], 'display': {'subtitle': 'category', 'highlights': ['identifier', 'status', 'granted_by']}, 'prior_art': [{'source': 'Wikidata — trademark (Q167270) / registered trademark (Q111048186)', 'url': 'https://www.wikidata.org/wiki/Q167270', 'notes': 'Trademark is a subclass of `intellectual property right` and of `mark`; holder via `owned by` (P127). registered-vs-pending is a status of one type, not a separate type — our `status` field.'}, {'source': 'WIPO Standard ST.96 — Trademark Components', 'url': 'https://www.wipo.int/standards/en/st96/v8-0/release_notes.html', 'notes': 'Canonical IP-office XML model. Source for mark, identifier, register, niceClass, status. Splits schemas by Trademark / Patent / Design Components — confirms `category` as the discriminator across one `intellectual_property` concept.'}, {'source': 'WIPO Standard ST.87 — IP event codes', 'url': 'https://www.wipo.int/standards/en/', 'notes': 'Standard lifecycle-event vocabulary (KeyEventCode). The filed/published/granted/lapsed milestones are dated links to the granting office, not node fields — events-as-links rule 1.'}, {'source': 'Nice Classification (Nice Agreement 1957; NCL 13-2026)', 'url': 'https://www.wipo.int/en/web/classification-nice', 'notes': '45-class system (1-34 goods, 35-45 services). `niceClass` is an integer[] of class numbers — a standard code. ADAVIA is Class 42.'}, {'source': 'USPTO — trademark process & intent-to-use basis', 'url': 'https://www.uspto.gov/trademarks/basics/trademark-process', 'notes': 'Lifecycle and the use-vs-intent-to-use fork. Source for the `status` value set and `filingBasis`.'}, {'source': 'schema.org/Intangible, schema.org/Brand', 'url': 'https://schema.org/Intangible', 'notes': 'Weak alignment — schema.org has no Trademark type; `Brand` is the marketing concept, not the legal right. Cited to mark the gap web ontologies leave: the IP right needs its own shape.'}]},
    'invitation': {'name': 'invitation', 'plural': 'invitations', 'description': 'An invitation to join something — an organization, a workspace, a team, a', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'acceptedAt', 'ty': 'datetime'}, {'name': 'allDay', 'ty': 'boolean'}, {'name': 'currentUrl', 'ty': 'string'}, {'name': 'dateUpdated', 'ty': 'datetime'}, {'name': 'distinctId', 'ty': 'string'}, {'name': 'email', 'ty': 'string'}, {'name': 'endDate', 'ty': 'datetime'}, {'name': 'icalUid', 'ty': 'string'}, {'name': 'invitationType', 'ty': 'string'}, {'name': 'message', 'ty': 'text'}, {'name': 'properties', 'ty': 'json'}, {'name': 'recurrence', 'ty': 'stringlist'}, {'name': 'revokedAt', 'ty': 'datetime'}, {'name': 'role', 'ty': 'string'}, {'name': 'showAs', 'ty': 'string'}, {'name': 'sourceTitle', 'ty': 'string'}, {'name': 'sourceUrl', 'ty': 'url'}, {'name': 'startDate', 'ty': 'datetime'}, {'name': 'status', 'ty': 'string'}, {'name': 'timezone', 'ty': 'string'}, {'name': 'token', 'ty': 'string'}, {'name': 'visibility', 'ty': 'string'}], 'also': ['event'], 'identity': ['at', 'id'], 'display': {'subtitle': 'invitationType', 'highlights': ['startDate', 'endDate', 'location']}, 'prior_art': [{'source': 'ActivityStreams 2.0 Invite activity', 'url': 'https://www.w3.org/TR/activitystreams-vocabulary/#dfn-invite', 'notes': 'AS2 Invite is the canonical fediverse verb. Our inviter = actor; invitee = target; status tracks Accept/Reject/TentativeAccept responses.'}, {'source': 'iCalendar ATTENDEE + PARTSTAT (RFC 5545)', 'url': 'https://datatracker.ietf.org/doc/html/rfc5545', 'notes': 'Calendar-style invitations. Our status maps to PARTSTAT (NEEDS-ACTION/ACCEPTED/DECLINED/DELEGATED).'}, {'source': 'SCIM 2.0 (RFC 7644) — user provisioning', 'url': 'https://datatracker.ietf.org/doc/html/rfc7644', 'notes': "Enterprise invitation/provisioning. Our email/role/organization align with SCIM User resource's email + entitlements + group membership."}]},
    'issue': {'name': 'issue', 'plural': 'issues', 'description': 'The demand atom of the product board — a problem, request, or observation.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'commentCount', 'ty': 'integer'}, {'name': 'community', 'ty': 'string'}, {'name': 'declined', 'ty': 'boolean'}, {'name': 'externalUrl', 'ty': 'url'}, {'name': 'postType', 'ty': 'string'}, {'name': 'score', 'ty': 'integer'}], 'derived': [{'key': 'downvotes', 'spec': {'count': 'for', 'where': {'direction': 'down'}}}, {'key': 'status', 'spec': {'reverse': 'addresses', 'get': 'status', 'prefer': ['achieved', 'active', 'at-risk', 'proposed'], 'map': {'achieved': 'addressed', 'active': 'in-progress', 'at-risk': 'in-progress', 'proposed': 'planned'}, 'default': 'open', 'authored': {'field': 'declined', 'equals': True, 'then': 'declined'}}}, {'key': 'upvotes', 'spec': {'count': 'for', 'where': {'direction': 'up'}}}, {'key': 'weight', 'spec': {'tally': 'for', 'by': 'direction', 'map': {'up': 1, 'down': -1}}}], 'also': ['post'], 'display': {'subtitle': 'status', 'highlights': ['status', 'weight']}, 'prior_art': [{'source': 'Linear issue + Customer Requests', 'url': 'https://linear.app/docs/customer-requests', 'notes': "An issue aggregates a request count rather than storing a status the team hand-maintains. Our weight ≈ the request count; status is derived from the addressing outcome's stage, never typed on the issue."}, {'source': 'Teresa Torres — Opportunity Solution Tree', 'url': 'https://www.producttalk.org/2016/08/opportunity-solution-tree/', 'notes': 'An opportunity (problem) is the citizen; solutions hang off it. Our issue is the opportunity; outcome `addresses` issue is the spine that makes a solution earn its existence.'}, {'source': 'Canny / Featurebase post', 'url': 'https://canny.io/', 'notes': 'The shipped atom is a demand item with a vote tally and a status lifecycle, grouped by status into a roadmap. issue (also post) + vote is that atom; the roadmap is this list grouped by derived status.'}]},
    'launch': {'name': 'launch', 'plural': 'launches', 'description': 'A rocket launch event. Carries flight-specific fields that previously', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'allDay', 'ty': 'boolean'}, {'name': 'articleUrl', 'ty': 'url'}, {'name': 'crewIds', 'ty': 'stringlist'}, {'name': 'currentUrl', 'ty': 'string'}, {'name': 'dateUpdated', 'ty': 'datetime'}, {'name': 'distinctId', 'ty': 'string'}, {'name': 'endDate', 'ty': 'datetime'}, {'name': 'flightNumber', 'ty': 'integer'}, {'name': 'icalUid', 'ty': 'string'}, {'name': 'landingOutcomes', 'ty': 'json'}, {'name': 'launchpadId', 'ty': 'string'}, {'name': 'patchImage', 'ty': 'url'}, {'name': 'properties', 'ty': 'json'}, {'name': 'recurrence', 'ty': 'stringlist'}, {'name': 'reusedBoosters', 'ty': 'stringlist'}, {'name': 'rocketId', 'ty': 'string'}, {'name': 'showAs', 'ty': 'string'}, {'name': 'sourceTitle', 'ty': 'string'}, {'name': 'sourceUrl', 'ty': 'url'}, {'name': 'startDate', 'ty': 'datetime'}, {'name': 'status', 'ty': 'string'}, {'name': 'timezone', 'ty': 'string'}, {'name': 'visibility', 'ty': 'string'}, {'name': 'webcastUrl', 'ty': 'url'}, {'name': 'wikipediaUrl', 'ty': 'url'}], 'also': ['event'], 'display': {'subtitle': 'rocketId', 'highlights': ['startDate', 'rocketId', 'launchpadId']}, 'prior_art': [{'source': 'SpaceX r/SpaceX API v4', 'url': 'https://github.com/r-spacex/SpaceX-API', 'notes': "Original source of these fields. The fly-by-night-launch.com app maps the v4 launches endpoint onto this shape; the per-booster landing outcomes JSON mirrors that API's `cores` sub-document."}]},
    'leg': {'name': 'leg', 'plural': 'legs', 'description': 'One continuous movement on a single vehicle — takeoff to landing,', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'allDay', 'ty': 'boolean'}, {'name': 'arrivalTime', 'ty': 'datetime'}, {'name': 'cabinClass', 'ty': 'string'}, {'name': 'carbonEmissions', 'ty': 'json'}, {'name': 'currentUrl', 'ty': 'string'}, {'name': 'dateUpdated', 'ty': 'datetime'}, {'name': 'departureTime', 'ty': 'datetime'}, {'name': 'distinctId', 'ty': 'string'}, {'name': 'duration', 'ty': 'string'}, {'name': 'durationMinutes', 'ty': 'integer'}, {'name': 'endDate', 'ty': 'datetime'}, {'name': 'flightNumber', 'ty': 'string'}, {'name': 'icalUid', 'ty': 'string'}, {'name': 'layoverMinutes', 'ty': 'integer'}, {'name': 'polyline', 'ty': 'string'}, {'name': 'properties', 'ty': 'json'}, {'name': 'recurrence', 'ty': 'stringlist'}, {'name': 'sequence', 'ty': 'integer'}, {'name': 'showAs', 'ty': 'string'}, {'name': 'sourceTitle', 'ty': 'string'}, {'name': 'sourceUrl', 'ty': 'url'}, {'name': 'startDate', 'ty': 'datetime'}, {'name': 'status', 'ty': 'string'}, {'name': 'timezone', 'ty': 'string'}, {'name': 'trace', 'ty': 'json'}, {'name': 'tracePointCount', 'ty': 'integer'}, {'name': 'vehicleType', 'ty': 'string'}, {'name': 'visibility', 'ty': 'string'}], 'also': ['event'], 'display': {'subtitle': 'flightNumber', 'highlights': ['startDate', 'endDate', 'location']}, 'prior_art': [{'source': 'IATA NDC "segment"', 'url': 'https://www.iata.org/en/programs/airline-distribution/retailing/ndc/', 'notes': 'NDC segment = our leg. flightNumber, departureTime, arrivalTime, cabinClass come straight from NDC OfferItem Segment.'}, {'source': 'GTFS stop_times.txt', 'url': 'https://gtfs.org/documentation/schedule/reference/#stop_timestxt', 'notes': 'Transit leg model. Our sequence = stop_sequence; departureTime/ arrivalTime = arrival_time/departure_time.'}, {'source': 'Google Encoded Polyline Algorithm', 'url': 'https://developers.google.com/maps/documentation/utilities/polylinealgorithmformat', 'notes': 'Our polyline field is the standard Google encoded polyline. trace is a denser GPS breadcrumb alternative (GeoJSON-adjacent).'}]},
    'list': {'name': 'list', 'plural': 'lists', 'description': 'A list — the universal ordered (or not) collection. Folders, menus,', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'arrangement', 'ty': 'string'}, {'name': 'default_view', 'ty': 'string'}, {'name': 'icon_size', 'ty': 'integer'}, {'name': 'isDefault', 'ty': 'boolean'}, {'name': 'isPublic', 'ty': 'boolean'}, {'name': 'itemCount', 'ty': 'integer'}, {'name': 'listId', 'ty': 'string'}, {'name': 'listType', 'ty': 'string'}, {'name': 'member_shape', 'ty': 'string'}, {'name': 'ordering_mode', 'ty': 'string'}, {'name': 'path', 'ty': 'string'}, {'name': 'privacy', 'ty': 'string'}, {'name': 'sort_by', 'ty': 'string'}], 'identity': ['at', 'id'], 'display': {'subtitle': 'name'}, 'prior_art': [{'source': 'schema.org/ItemList', 'url': 'https://schema.org/ItemList', 'notes': 'listType ≈ itemListOrder; contains ≈ itemListElement; isPublic ≈ publicAccess.'}, {'source': 'ActivityStreams 2.0 Collection / OrderedCollection', 'url': 'https://www.w3.org/TR/activitystreams-vocabulary/#dfn-collection', 'notes': "contains[] ≈ items; ordering_mode='linear' ≈ OrderedCollection, ordering_mode='unordered' ≈ Collection."}, {'source': 'WinFS Item / FolderMember', 'url': 'https://learn.microsoft.com/en-us/archive/msdn-magazine/2004/january/winfs-lets-users-search-and-manage-files-based-on-content', 'notes': 'WinFS unified Folder + Contact + Photo under a single Item base, with FolderMember as a holding link. Our list-with-contains is the same pattern: one shape, one link mechanism, view-time projections handle the "I want it to look like an album" case.'}, {'source': 'Vannevar Bush — As We May Think (Memex trails)', 'url': 'https://www.theatlantic.com/magazine/archive/1945/07/as-we-may-think/303881/', 'notes': "A Memex trail is a named, ordered list of associative jumps. A `list` with ordering_mode='linear' and contains-bookmarks IS Bush's trail. Foundational precedent for the everything-is-a-list thesis."}, {'source': 'POSIX / Single Unix Specification (directories)', 'url': 'https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap03.html', 'notes': "listType='folder' with optional `path` field mirrors a POSIX directory. The engine treats it as a list; the filesystem mirror is a projection, not a separate primitive."}]},
    'loaded_model': {'name': 'loaded_model', 'plural': 'loaded_models', 'description': 'A currently loaded/running AI model instance.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'allDay', 'ty': 'boolean'}, {'name': 'currentUrl', 'ty': 'string'}, {'name': 'dateUpdated', 'ty': 'datetime'}, {'name': 'digest', 'ty': 'string'}, {'name': 'distinctId', 'ty': 'string'}, {'name': 'endDate', 'ty': 'datetime'}, {'name': 'icalUid', 'ty': 'string'}, {'name': 'properties', 'ty': 'json'}, {'name': 'quantization', 'ty': 'string'}, {'name': 'recurrence', 'ty': 'stringlist'}, {'name': 'showAs', 'ty': 'string'}, {'name': 'size', 'ty': 'string'}, {'name': 'sizeVram', 'ty': 'integer'}, {'name': 'sourceTitle', 'ty': 'string'}, {'name': 'sourceUrl', 'ty': 'url'}, {'name': 'startDate', 'ty': 'datetime'}, {'name': 'status', 'ty': 'string'}, {'name': 'timezone', 'ty': 'string'}, {'name': 'visibility', 'ty': 'string'}, {'name': 'vramUsage', 'ty': 'string'}], 'also': ['event'], 'display': {'subtitle': 'size', 'highlights': ['startDate', 'endDate', 'location']}, 'prior_art': [{'source': 'Ollama API — /api/ps', 'url': 'https://github.com/ollama/ollama/blob/main/docs/api.md#list-running-models', 'notes': "Direct source. Our size/vramUsage/sizeVram/quantization/digest/ expiresAt map to Ollama's ListRunningModelsResponse fields."}, {'source': 'OpenTelemetry Resource semconv (ML/AI)', 'url': 'https://opentelemetry.io/docs/specs/semconv/gen-ai/', 'notes': 'Emerging conventions for GenAI observability. Our size/digest align with gen_ai.model.* resource attributes.'}]},
    'mcp_session': {'name': 'mcp_session', 'plural': 'mcp_sessions', 'description': 'An MCP session — a client connected, made some calls, disconnected.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'client', 'ty': 'string', 'required': True}, {'name': 'endedAt', 'ty': 'datetime'}, {'name': 'gitBranch', 'ty': 'string', 'required': True}, {'name': 'messageCount', 'ty': 'integer'}, {'name': 'projectId', 'ty': 'string', 'required': True}, {'name': 'sessionType', 'ty': 'string'}, {'name': 'startedAt', 'ty': 'datetime'}, {'name': 'tokenCount', 'ty': 'integer'}], 'identity': ['client', 'projectId', 'gitBranch'], 'display': {'subtitle': 'client'}, 'prior_art': [{'source': 'Model Context Protocol (MCP) session', 'url': 'https://modelcontextprotocol.io/specification', 'notes': "Direct source. Our client/sessionType come from MCP's client/transport concepts (STDIO, HTTP+SSE)."}, {'source': 'OpenTelemetry Spans (root span ≈ session)', 'url': 'https://opentelemetry.io/docs/concepts/signals/traces/', 'notes': 'Our startedAt/endedAt/messageCount/tokenCount align with span lifecycle + attributes in a trace context.'}, {'source': 'OpenID Connect Session Management 1.0', 'url': 'https://openid.net/specs/openid-connect-session-1_0.html', 'notes': 'Classical web-session model. Our participant ≈ authenticated subject; projectId/gitBranch are AgentOS-specific scoping.'}]},
    'measure': {'name': 'measure', 'plural': 'measures', 'description': 'A single measured value about a subject, at a time — "LDL = 95 mg/dL on', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'allDay', 'ty': 'boolean'}, {'name': 'currentUrl', 'ty': 'string'}, {'name': 'dateUpdated', 'ty': 'datetime'}, {'name': 'distinctId', 'ty': 'string'}, {'name': 'endDate', 'ty': 'datetime'}, {'name': 'flag', 'ty': 'string'}, {'name': 'icalUid', 'ty': 'string'}, {'name': 'notes', 'ty': 'text'}, {'name': 'properties', 'ty': 'json'}, {'name': 'recurrence', 'ty': 'stringlist'}, {'name': 'refHigh', 'ty': 'number'}, {'name': 'refLow', 'ty': 'number'}, {'name': 'refText', 'ty': 'string'}, {'name': 'showAs', 'ty': 'string'}, {'name': 'sourceTitle', 'ty': 'string'}, {'name': 'sourceUrl', 'ty': 'url'}, {'name': 'startDate', 'ty': 'datetime'}, {'name': 'status', 'ty': 'string'}, {'name': 'timezone', 'ty': 'string'}, {'name': 'value', 'ty': 'number'}, {'name': 'valueText', 'ty': 'string'}, {'name': 'visibility', 'ty': 'string'}], 'also': ['event'], 'display': {'subtitle': 'startDate', 'highlights': ['startDate', 'endDate', 'location']}, 'prior_art': [{'source': 'HL7 FHIR R5 — Observation', 'url': 'https://www.hl7.org/fhir/observation.html', 'notes': 'The canonical resource for a measured value. value (with its UCUM unit) ≈ valueQuantity; startDate ≈ effectiveDateTime; refLow/refHigh/refText ≈ the referenceRange backbone (the inline snapshot); flag ≈ interpretation; status ≈ status. `measures` ≈ code resolved to a biomarker. FHIR has no normalized-range link — our `reportedRange` link adds that.'}, {'source': 'HL7 v2.x — OBX segment', 'url': 'https://hl7-definition.caristix.com/v2/HL7v2.5/Segments/OBX', 'notes': 'The legacy lab-result segment most labs still emit. OBX-5 (value) and OBX-6 (units) together ≈ our value-with-unit; OBX-7 (reference range), OBX-8 (abnormal flag), OBX-14 (datetime) map to refText/flag/startDate.'}, {'source': 'UCUM — Unified Code for Units of Measure', 'url': 'https://ucum.org/', 'notes': 'The unit on every numeric val (mg/dL, mmol/L, 10*3/uL) follows UCUM — the unit system FHIR mandates for Observation.valueQuantity, so measures round-trip into FHIR cleanly.'}]},
    'meeting': {'name': 'meeting', 'plural': 'meetings', 'description': 'A calendar meeting — an event with virtual meeting details and transcripts.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'allDay', 'ty': 'boolean'}, {'name': 'calendarLink', 'ty': 'url'}, {'name': 'conferenceProvider', 'ty': 'string'}, {'name': 'currentUrl', 'ty': 'string'}, {'name': 'dateUpdated', 'ty': 'datetime'}, {'name': 'distinctId', 'ty': 'string'}, {'name': 'endDate', 'ty': 'datetime'}, {'name': 'icalUid', 'ty': 'string'}, {'name': 'isVirtual', 'ty': 'boolean'}, {'name': 'meetingType', 'ty': 'string'}, {'name': 'meetingUrl', 'ty': 'url'}, {'name': 'phoneDialIn', 'ty': 'string'}, {'name': 'properties', 'ty': 'json'}, {'name': 'recurrence', 'ty': 'stringlist'}, {'name': 'showAs', 'ty': 'string'}, {'name': 'sourceTitle', 'ty': 'string'}, {'name': 'sourceUrl', 'ty': 'url'}, {'name': 'startDate', 'ty': 'datetime'}, {'name': 'status', 'ty': 'string'}, {'name': 'timezone', 'ty': 'string'}, {'name': 'visibility', 'ty': 'string'}], 'also': ['event'], 'display': {'subtitle': 'location', 'highlights': ['startDate', 'endDate', 'location']}, 'prior_art': [{'source': 'RFC 5545 VEVENT + conference property (RFC 7986)', 'url': 'https://datatracker.ietf.org/doc/html/rfc7986#section-5.11', 'notes': 'Our meetingUrl ≈ CONFERENCE URI; phoneDialIn = tel: URI in CONFERENCE feature=PHONE; conferenceProvider ≈ CONFERENCE LABEL.'}, {'source': 'schema.org/Event — location.VirtualLocation', 'url': 'https://schema.org/VirtualLocation', 'notes': 'Our isVirtual triggers VirtualLocation; meetingUrl ≈ VirtualLocation.url.'}, {'source': 'Google Calendar Event conferenceData', 'url': 'https://developers.google.com/calendar/api/v3/reference/events', 'notes': 'Practical API mirror. Our conferenceProvider ≈ conferenceData.conferenceSolution.name; meetingUrl = entryPoints[uri].'}]},
    'membership': {'name': 'membership', 'plural': 'memberships', 'description': 'A time-bounded right-of-belonging granted by an organization.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'allDay', 'ty': 'boolean'}, {'name': 'autoRenew', 'ty': 'boolean'}, {'name': 'billingType', 'ty': 'string'}, {'name': 'currency', 'ty': 'string'}, {'name': 'currentUrl', 'ty': 'string'}, {'name': 'dateUpdated', 'ty': 'datetime'}, {'name': 'distinctId', 'ty': 'string'}, {'name': 'endDate', 'ty': 'datetime'}, {'name': 'guestPassQuantity', 'ty': 'integer'}, {'name': 'icalUid', 'ty': 'string'}, {'name': 'price', 'ty': 'number'}, {'name': 'properties', 'ty': 'json'}, {'name': 'recurrence', 'ty': 'stringlist'}, {'name': 'showAs', 'ty': 'string'}, {'name': 'sourceTitle', 'ty': 'string'}, {'name': 'sourceUrl', 'ty': 'url'}, {'name': 'startDate', 'ty': 'datetime'}, {'name': 'status', 'ty': 'string'}, {'name': 'tier', 'ty': 'string'}, {'name': 'timezone', 'ty': 'string'}, {'name': 'useCount', 'ty': 'integer'}, {'name': 'visibility', 'ty': 'string'}], 'also': ['event'], 'identity': ['at', 'id'], 'display': {'subtitle': 'status', 'highlights': ['startDate', 'endDate', 'location']}, 'prior_art': [{'source': 'schema.org/ProgramMembership', 'url': 'https://schema.org/ProgramMembership', 'notes': "schema.org's canonical membership type. Our member = member; plan ≈ programName/membershipNumber; at ≈ hostingOrganization. ProgramMembership covers gym, loyalty, society memberships without requiring a billing cycle — matches our non-commercial framing."}, {'source': 'schema.org/Subscription', 'url': 'https://schema.org/Subscription', 'notes': 'Streaming/SaaS subscriptions fit this shape — one model covers gym memberships and Spotify Premium. billingType maps to billingPeriod; autoRenew maps directly.'}, {'source': 'Stripe Subscriptions API', 'url': 'https://docs.stripe.com/api/subscriptions', 'notes': 'Practical API mirror for commercial memberships. Our status values (active/paused/cancelled/past_due) mirror Stripe Subscription.status. nextBillDate ≈ current_period_end.'}, {'source': 'Mindbody Contracts/Memberships', 'url': 'https://developers.mindbodyonline.com/PublicDocumentation/V6', 'notes': "Gym-industry API. Our useCount, guestPassQuantity, startEffectiveDate / endEffectiveDate are lifted from Mindbody's Membership record shape."}, {'source': 'FOAF member / membershipClass', 'url': 'http://xmlns.com/foaf/spec/#term_member', 'notes': 'Social-web vocabulary for "X is a member of Y". Our member ↔ at link mirrors foaf:member; our tier ≈ foaf:membershipClass.'}]},
    'message': {'name': 'message', 'plural': 'messages', 'description': 'A single message in a conversation. Base type — email extends this via `also`.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'conversationId', 'ty': 'string'}, {'name': 'isOutgoing', 'ty': 'boolean'}, {'name': 'isStarred', 'ty': 'boolean'}], 'identity': ['at', 'id'], 'display': {'subtitle': 'from'}, 'prior_art': [{'source': 'ActivityStreams 2.0 Note/Activity', 'url': 'https://www.w3.org/TR/activitystreams-vocabulary/#dfn-note', 'notes': 'Closest open standard for generic messages. Our from ≈ actor; inConversation ≈ context/conversation; repliesTo ≈ inReplyTo.'}, {'source': 'Matrix m.room.message', 'url': 'https://spec.matrix.org/latest/client-server-api/#mroommessage', 'notes': 'Practical cross-platform message event schema. Our isOutgoing has no Matrix analog (sender identity instead); repliesTo ≈ m.relates_to rel_type m.thread/m.in_reply_to.'}, {'source': 'XMPP (RFC 6121) message stanza', 'url': 'https://datatracker.ietf.org/doc/html/rfc6121', 'notes': 'IETF instant-messaging baseline. from/to/thread correspond to our from/inConversation; no standardized isStarred.'}]},
    'model': {'name': 'model', 'plural': 'models', 'description': 'An AI model — LLM, embedding model, or other ML model.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'contextLength', 'ty': 'integer'}, {'name': 'contextWindow', 'ty': 'integer'}, {'name': 'digest', 'ty': 'string'}, {'name': 'family', 'ty': 'string'}, {'name': 'format', 'ty': 'string'}, {'name': 'maxOutput', 'ty': 'integer'}, {'name': 'modality', 'ty': 'stringlist'}, {'name': 'modelType', 'ty': 'string'}, {'name': 'parameterSize', 'ty': 'string'}, {'name': 'pricingInput', 'ty': 'string'}, {'name': 'pricingOutput', 'ty': 'string'}, {'name': 'quantization', 'ty': 'string'}, {'name': 'quantizationLevel', 'ty': 'string'}, {'name': 'size', 'ty': 'string'}], 'identity': ['at', 'name'], 'display': {'subtitle': 'name'}, 'prior_art': [{'source': 'Hugging Face Model Cards', 'url': 'https://huggingface.co/docs/hub/en/model-cards', 'notes': 'Our provider/contextLength/modality/family/quantization/ parameterSize align with HF model-card metadata conventions.'}, {'source': 'Ollama /api/show + Modelfile', 'url': 'https://github.com/ollama/ollama/blob/main/docs/modelfile.md', 'notes': "Our quantization/quantizationLevel/format/digest/parameterSize come directly from Ollama's show-model response."}, {'source': 'OpenRouter Models API', 'url': 'https://openrouter.ai/docs/models', 'notes': "Our contextLength/contextWindow/maxOutput/pricingInput/ pricingOutput mirror OpenRouter's model spec."}]},
    'module': {'name': 'module', 'plural': 'modules', 'description': 'A self-contained unit of a larger whole — a software module, a course', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'path', 'ty': 'string'}, {'name': 'planned', 'ty': 'boolean'}, {'name': 'role', 'ty': 'text'}, {'name': 'status', 'ty': 'string'}, {'name': 'version', 'ty': 'string'}], 'display': {'subtitle': 'role', 'highlights': ['status', 'path']}, 'prior_art': [{'source': 'schema.org hasPart / isPartOf (Course modules)', 'url': 'https://schema.org/hasPart', 'notes': 'Course.hasPart models course modules; hasPart/isPartOf are the inverse composition edges, reusable for any whole/part.'}, {'source': 'UML 2.5 Component (OMG)', 'url': 'https://www.uml-diagrams.org/component.html', 'notes': 'A component is a "modular part with encapsulated content, replaceable within its environment" → role + depends_on.'}, {'source': 'SPDX Package', 'url': 'https://spdx.dev/', 'notes': 'A package is a versioned, named unit with declared dependencies → version + depends_on, across software and hardware domains.'}]},
    'note': {'name': 'note', 'plural': 'notes', 'description': 'Private text content, primarily for the author. Journal entries, PKM notes,', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'isPinned', 'ty': 'boolean'}, {'name': 'noteType', 'ty': 'string'}], 'display': {'subtitle': 'noteType'}, 'prior_art': [{'source': 'Zettelkasten / Luhmann slip-box', 'url': 'https://zettelkasten.de/overview/', 'notes': "Our noteType (fleeting/literature/permanent) is the canonical Zettelkasten triad; references[] ≈ Luhmann's permanent links."}, {'source': 'W3C Web Annotation Data Model', 'url': 'https://www.w3.org/TR/annotation-model/', 'notes': 'Our extractedFrom = target; createdBy = creator. Notes are annotations without a structured position selector.'}, {'source': 'Obsidian / Roam / Logseq PKM conventions', 'url': 'https://obsidian.md/', 'notes': 'Practical PKM lineage. isPinned/noteType mirror the "pinned/daily/permanent" UX of modern note apps.'}]},
    'offer': {'name': 'offer', 'plural': 'offers', 'description': 'A purchasable offer — typically a flight itinerary with a price.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'allDay', 'ty': 'boolean'}, {'name': 'availability', 'ty': 'string'}, {'name': 'bookingToken', 'ty': 'string'}, {'name': 'currency', 'ty': 'string'}, {'name': 'currentUrl', 'ty': 'string'}, {'name': 'dateUpdated', 'ty': 'datetime'}, {'name': 'departureToken', 'ty': 'string'}, {'name': 'distinctId', 'ty': 'string'}, {'name': 'endDate', 'ty': 'datetime'}, {'name': 'icalUid', 'ty': 'string'}, {'name': 'offerType', 'ty': 'string'}, {'name': 'price', 'ty': 'number'}, {'name': 'properties', 'ty': 'json'}, {'name': 'recurrence', 'ty': 'stringlist'}, {'name': 'showAs', 'ty': 'string'}, {'name': 'sourceTitle', 'ty': 'string'}, {'name': 'sourceUrl', 'ty': 'url'}, {'name': 'startDate', 'ty': 'datetime'}, {'name': 'status', 'ty': 'string'}, {'name': 'timezone', 'ty': 'string'}, {'name': 'visibility', 'ty': 'string'}], 'also': ['event'], 'identity': ['id'], 'display': {'subtitle': 'price', 'highlights': ['startDate', 'endDate', 'location']}, 'prior_art': [{'source': 'schema.org/Offer', 'url': 'https://schema.org/Offer', 'notes': 'Our price = price; currency = priceCurrency; availability = availability; validFrom/validUntil match directly.'}, {'source': 'IATA NDC OfferItem', 'url': 'https://www.iata.org/en/programs/airline-distribution/retailing/ndc/', 'notes': 'Our bookingToken ≈ OfferItemID; validUntil ≈ TimeLimits/ OfferExpirationDateTime; trips[] ≈ Itinerary.'}, {'source': 'schema.org/AggregateOffer', 'url': 'https://schema.org/AggregateOffer', 'notes': 'For price-range offers (SerpAPI flight results). offerType is AgentOS-specific.'}]},
    'order': {'name': 'order', 'plural': 'orders', 'description': 'A purchase order. Contains products and tracks delivery.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'allDay', 'ty': 'boolean'}, {'name': 'body', 'ty': 'text'}, {'name': 'currency', 'ty': 'string'}, {'name': 'currentUrl', 'ty': 'string'}, {'name': 'dateUpdated', 'ty': 'datetime'}, {'name': 'deliveryDate', 'ty': 'datetime'}, {'name': 'deliveryFee', 'ty': 'number'}, {'name': 'deliveryInstructions', 'ty': 'string'}, {'name': 'distinctId', 'ty': 'string'}, {'name': 'endDate', 'ty': 'datetime'}, {'name': 'eta', 'ty': 'string'}, {'name': 'fareBreakdown', 'ty': 'json'}, {'name': 'head', 'ty': 'text'}, {'name': 'icalUid', 'ty': 'string'}, {'name': 'interactionType', 'ty': 'string'}, {'name': 'itemStates', 'ty': 'json'}, {'name': 'latestArrival', 'ty': 'datetime'}, {'name': 'messages', 'ty': 'json'}, {'name': 'orderDate', 'ty': 'datetime'}, {'name': 'orderId', 'ty': 'string', 'required': True}, {'name': 'orderUuid', 'ty': 'string'}, {'name': 'originalTotal', 'ty': 'string'}, {'name': 'originalTotalAmount', 'ty': 'number'}, {'name': 'progress', 'ty': 'number'}, {'name': 'progressTotal', 'ty': 'number'}, {'name': 'properties', 'ty': 'json'}, {'name': 'recurrence', 'ty': 'stringlist'}, {'name': 'savings', 'ty': 'number'}, {'name': 'showAs', 'ty': 'string'}, {'name': 'sourceTitle', 'ty': 'string'}, {'name': 'sourceUrl', 'ty': 'url'}, {'name': 'startDate', 'ty': 'datetime'}, {'name': 'status', 'ty': 'string'}, {'name': 'subtotal', 'ty': 'number'}, {'name': 'summary', 'ty': 'string'}, {'name': 'taxes', 'ty': 'number'}, {'name': 'timeline', 'ty': 'json'}, {'name': 'timezone', 'ty': 'string'}, {'name': 'tipAmount', 'ty': 'number'}, {'name': 'total', 'ty': 'string'}, {'name': 'totalAmount', 'ty': 'number'}, {'name': 'visibility', 'ty': 'string'}], 'also': ['event'], 'identity': ['at', 'orderId'], 'display': {'subtitle': 'total', 'highlights': ['startDate', 'endDate', 'location']}, 'prior_art': [{'source': 'schema.org/Order', 'url': 'https://schema.org/Order', 'notes': 'Our orderId = orderNumber; orderDate = orderDate; total = totalPaymentDue; status = orderStatus; shippingAddress = orderDelivery.'}, {'source': 'schema.org/OrderStatus (enum)', 'url': 'https://schema.org/OrderStatus', 'notes': 'Our status values (placed, confirmed, delivering, completed, cancelled) map to OrderProcessing/OrderInTransit/OrderDelivered/ OrderCancelled.'}, {'source': 'Amazon Order Reports (MWS / SP-API)', 'url': 'https://developer-docs.amazon.com/sp-api/docs/orders-api-v0-reference', 'notes': 'Practical source. Our orderId, fareBreakdown, savings, eta are lifted from Amazon/Uber Eats order structures.'}]},
    'organization': {'name': 'organization', 'plural': 'organizations', 'description': 'A company, nonprofit, or other organization. Organizations are actors — they', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'actorType', 'ty': 'string'}, {'name': 'industry', 'ty': 'string'}], 'also': ['actor'], 'identity': ['name'], 'display': {'subtitle': 'industry', 'image': 'image', 'highlights': ['headquarters']}, 'prior_art': [{'source': 'schema.org/Organization', 'url': 'https://schema.org/Organization', 'notes': "Our industry ≈ naics/isicV4 (loosely); founded = foundingDate; member[] = member; headquarters = location; parentOrganization maps directly (schema.org's subOrganization is its declared inverse)."}, {'source': 'vCard 4.0 KIND=org (RFC 6350)', 'url': 'https://datatracker.ietf.org/doc/html/rfc6350', 'notes': 'Organization-as-contact. Our website/domain ≈ URL; headquarters ≈ ADR. Thinner than schema.org for industry/founded.'}, {'source': 'Wikidata (Organization, Q43229)', 'url': 'https://www.wikidata.org/wiki/Q43229', 'notes': 'Cross-reference identity. Useful for deduping; no direct field alignment but industry maps to P452 (industry) and founded to P571 (inception).'}]},
    'outcome': {'name': 'outcome', 'plural': 'outcomes', 'description': 'A tracked target-state — the change being sought, with a status and', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'archived', 'ty': 'boolean'}, {'name': 'baseline', 'ty': 'string'}, {'name': 'current', 'ty': 'string'}, {'name': 'metric', 'ty': 'string'}, {'name': 'priority', 'ty': 'integer'}, {'name': 'statement', 'ty': 'text'}, {'name': 'status', 'ty': 'string'}, {'name': 'target', 'ty': 'string'}], 'display': {'subtitle': 'status', 'body': 'statement', 'highlights': ['status', 'priority']}, 'prior_art': [{'source': 'John Doerr, "Measure What Matters" (OKR)', 'url': 'https://www.whatmatters.com/faqs/okr-meaning-definition-example', 'notes': 'Objective → statement; Key Result → the metric/baseline/current/target quad ("I will X as measured by Y").'}, {'source': 'W.K. Kellogg Foundation Logic Model Development Guide', 'url': 'https://www.nj.gov/state/assets/pdf/ofbi/kellogg-foundation-logic-model-development-guide.pdf', 'notes': 'Outcomes as short/intermediate/long-term changes in a causal chain → the depends_on / advances edges.'}, {'source': 'schema.org/AchieveAction + result', 'url': 'https://schema.org/AchieveAction', 'notes': 'Closest schema.org neighbor, but `result` models what an action produced, not a tracked target-state — so outcome is its own type.'}]},
    'pass': {'name': 'pass', 'plural': 'passes', 'description': 'A fixed-quantity right-of-access — a bundle of entries, a multi-day', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'allDay', 'ty': 'boolean'}, {'name': 'boardingGroup', 'ty': 'string'}, {'name': 'checkinStatus', 'ty': 'string'}, {'name': 'currency', 'ty': 'string'}, {'name': 'currentUrl', 'ty': 'string'}, {'name': 'dateUpdated', 'ty': 'datetime'}, {'name': 'distinctId', 'ty': 'string'}, {'name': 'endDate', 'ty': 'datetime'}, {'name': 'gate', 'ty': 'string'}, {'name': 'icalUid', 'ty': 'string'}, {'name': 'isAllDayPass', 'ty': 'boolean'}, {'name': 'nameOnTicket', 'ty': 'string'}, {'name': 'price', 'ty': 'number'}, {'name': 'properties', 'ty': 'json'}, {'name': 'purchasedQuantity', 'ty': 'integer'}, {'name': 'quantity', 'ty': 'integer'}, {'name': 'recurrence', 'ty': 'stringlist'}, {'name': 'seatAssignment', 'ty': 'string'}, {'name': 'showAs', 'ty': 'string'}, {'name': 'sourceTitle', 'ty': 'string'}, {'name': 'sourceUrl', 'ty': 'url'}, {'name': 'startDate', 'ty': 'datetime'}, {'name': 'status', 'ty': 'string'}, {'name': 'terminal', 'ty': 'string'}, {'name': 'ticketClass', 'ty': 'string'}, {'name': 'ticketNumber', 'ty': 'string'}, {'name': 'timezone', 'ty': 'string'}, {'name': 'useCount', 'ty': 'integer'}, {'name': 'visibility', 'ty': 'string'}], 'also': ['event'], 'identity': ['at', 'id'], 'display': {'subtitle': 'status', 'highlights': ['startDate', 'endDate', 'location']}, 'prior_art': [{'source': 'schema.org/Ticket', 'url': 'https://schema.org/Ticket', 'notes': "schema.org's peer for a claim-check right-of-entry. Our purchasedDate = issuedAt; holder = underName; price matches directly. Ticket is event-bound; we generalize to any right-of-use."}, {'source': 'Mindbody Services (pricing options)', 'url': 'https://developers.mindbodyonline.com/PublicDocumentation/V6', 'notes': "Gym-industry reference. Our quantity/purchasedQuantity/ useCount/depletedDate are lifted from Mindbody's ClientService.Remaining / Count / DateCompleted."}, {'source': 'GTFS fare rules / IATA fare basis', 'url': 'https://gtfs.org/documentation/schedule/reference/#fare_productstxt', 'notes': 'Transit-pass vocabulary: single-ride, day-pass, period-pass all fit `isAllDayPass` + `startEffectiveDate` + `endEffectiveDate`.'}]},
    'payment_method': {'name': 'payment_method', 'plural': 'payment_methods', 'description': 'A saved payment instrument — credit/debit card, PayPal/Venmo account,', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'balance', 'ty': 'number'}, {'name': 'binRange', 'ty': 'string'}, {'name': 'brand', 'ty': 'string'}, {'name': 'currency', 'ty': 'string'}, {'name': 'customDescription', 'ty': 'string'}, {'name': 'displayName', 'ty': 'string'}, {'name': 'expMonth', 'ty': 'integer'}, {'name': 'expYear', 'ty': 'integer'}, {'name': 'expirationDate', 'ty': 'string'}, {'name': 'fingerprint', 'ty': 'string'}, {'name': 'holderName', 'ty': 'string'}, {'name': 'identifier', 'ty': 'string', 'required': True}, {'name': 'isDefault', 'ty': 'boolean'}, {'name': 'isExpired', 'ty': 'boolean'}, {'name': 'isPrimary', 'ty': 'boolean'}, {'name': 'isSelected', 'ty': 'boolean'}, {'name': 'last4', 'ty': 'string'}, {'name': 'metadata', 'ty': 'json'}, {'name': 'providerTokens', 'ty': 'json'}, {'name': 'status', 'ty': 'string'}, {'name': 'subtype', 'ty': 'string'}, {'name': 'type', 'ty': 'string'}], 'identity': ['at', 'identifier'], 'display': {'subtitle': 'displayName'}, 'prior_art': [{'source': 'Stripe PaymentMethod API', 'url': 'https://docs.stripe.com/api/payment_methods/object', 'notes': "The gold standard. Our type/subtype ≈ Stripe's `type` + `card.brand`; last4/expMonth/expYear/fingerprint map 1:1 to `card.last4/exp_month/exp_year/fingerprint`. Stripe's billing_details is our `billingAddress` relation. Stripe's `pm_xxx` id is the canonical opaque handle."}, {'source': 'PCI DSS v4.0 Requirement 3 (Protect Stored Account Data)', 'url': 'https://www.pcisecuritystandards.org/document_library/', 'notes': "Defines what's storable: PAN truncated, expiry, cardholder name, service code. FORBIDS full PAN (unencrypted), CVV/CVC2/CID, PIN/PIN block, track data. This shape carries only the permitted subset. Opaque tokens are NOT card data under PCI — they're the merchant/provider's detokenization references; storing them is the recommended mitigation (Req. 3.5 tokenization)."}, {'source': 'IATA Resolution 890 / PADIS Form-of-Payment codes', 'url': 'https://www.iata.org/en/publications/store/passenger-and-baggage-tariffs/', 'notes': 'Source for the airline 2-char `subtype` codes: AX (Amex), VI (Visa), MC (MasterCard), DS (Discover), DC (Diners), TP (UATP), JC (JCB), UP (UnionPay). These are the codes embedded in PNR FOP fields and EMD records. We keep them verbatim so airline checkout round-trips work without translation.'}, {'source': 'W3C Payment Request API / Payment Method Identifiers', 'url': 'https://www.w3.org/TR/payment-method-id/', 'notes': 'Browser-standard payment abstraction. `basic-card`, `https://apple.com/apple-pay`, `https://google.com/pay`, `https://paypal.com` are the method identifiers — our type/subtype combo is a normalized form.'}, {'source': 'Apple Pay Payment Token / Google Pay Network Token', 'url': 'https://developer.apple.com/documentation/passkit/apple_pay/payment_token_format_reference', 'notes': "Device-bound token replaces the PAN on-chain. The DPAN and cryptogram live in `providerTokens`; `last4` on the wallet surfaces the DEVICE last-4, not the funding card's last-4."}, {'source': 'schema.org/PaymentMethod + LoyaltyProgram', 'url': 'https://schema.org/PaymentMethod', 'notes': "schema.org's PaymentMethod is a thin enum (CreditCard, Cash, PaymentCard, ByInvoice). We extend it into a real shape with tokens and holder. Our `type` overlaps its enumeration values."}, {'source': 'PayPal Billing Agreements / Vault', 'url': 'https://developer.paypal.com/docs/multiparty/vault/', 'notes': "PayPal's saved-method pattern — billingAgreementId is the opaque handle, used like our `providerTokens`. Payer given_name → `holderName`. No last4 (PayPal-as-wallet has no card number surface); our shape accommodates via nullable last4."}, {'source': 'EMVCo Tokenisation Framework v2.0', 'url': 'https://www.emvco.com/specifications/payment-tokenisation/', 'notes': 'Industry spec for network tokens (Visa Token Service, Mastercard MDES). Defines token requestor, token reference id, PAR (Payment Account Reference) — PAR is the cross-token dedupe primitive our `fingerprint` field aligns with when the provider surfaces it.'}]},
    'person': {'name': 'person', 'plural': 'people', 'description': 'A real human. People are actors — they can own accounts, hold roles,', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'about', 'ty': 'text'}, {'name': 'actorType', 'ty': 'string'}, {'name': 'notes', 'ty': 'text'}], 'derived': [{'key': 'additionalName', 'spec': {'latest': [{'find': 'born_in', 'is': 'birth', 'get': 'additionalName'}, {'find': 'changed', 'is': 'transition', 'get': 'additionalName'}]}}, {'key': 'birthdate', 'spec': {'find': 'born_in', 'is': 'birth', 'get': 'startDate'}}, {'key': 'current_residence', 'spec': {'find': 'lived_at', 'where_link': {'to': None}, 'get': 'name'}}, {'key': 'current_role', 'spec': {'find': 'worked_at', 'where_link': {'to': None}, 'get': 'title'}}, {'key': 'familyName', 'spec': {'latest': [{'find': 'born_in', 'is': 'birth', 'get': 'familyName'}, {'find': 'changed', 'is': 'transition', 'get': 'familyName'}]}}, {'key': 'gender', 'spec': {'latest': [{'find': 'born_in', 'is': 'birth', 'get': 'gender'}, {'find': 'changed', 'is': 'transition', 'get': 'gender'}]}}, {'key': 'givenName', 'spec': {'latest': [{'find': 'born_in', 'is': 'birth', 'get': 'givenName'}, {'find': 'changed', 'is': 'transition', 'get': 'givenName'}]}}, {'key': 'honorificPrefix', 'spec': {'latest': [{'find': 'born_in', 'is': 'birth', 'get': 'honorificPrefix'}, {'find': 'changed', 'is': 'transition', 'get': 'honorificPrefix'}]}}, {'key': 'honorificSuffix', 'spec': {'latest': [{'find': 'born_in', 'is': 'birth', 'get': 'honorificSuffix'}, {'find': 'changed', 'is': 'transition', 'get': 'honorificSuffix'}]}}, {'key': 'legalName', 'spec': {'latest': [{'find': 'born_in', 'is': 'birth', 'get': 'legalName'}, {'find': 'changed', 'is': 'transition', 'get': 'legalName'}]}}, {'key': 'maidenName', 'spec': {'latest': [{'find': 'born_in', 'is': 'birth', 'get': 'maidenName'}, {'find': 'changed', 'is': 'transition', 'get': 'maidenName'}]}}, {'key': 'nameOrder', 'spec': {'latest': [{'find': 'born_in', 'is': 'birth', 'get': 'nameOrder'}, {'find': 'changed', 'is': 'transition', 'get': 'nameOrder'}]}}, {'key': 'nickname', 'spec': {'latest': [{'find': 'born_in', 'is': 'birth', 'get': 'nickname'}, {'find': 'changed', 'is': 'transition', 'get': 'nickname'}]}}, {'key': 'phoneticFamilyName', 'spec': {'latest': [{'find': 'born_in', 'is': 'birth', 'get': 'phoneticFamilyName'}, {'find': 'changed', 'is': 'transition', 'get': 'phoneticFamilyName'}]}}, {'key': 'phoneticGivenName', 'spec': {'latest': [{'find': 'born_in', 'is': 'birth', 'get': 'phoneticGivenName'}, {'find': 'changed', 'is': 'transition', 'get': 'phoneticGivenName'}]}}, {'key': 'sortAs', 'spec': {'latest': [{'find': 'born_in', 'is': 'birth', 'get': 'sortAs'}, {'find': 'changed', 'is': 'transition', 'get': 'sortAs'}]}}], 'shortcuts': [{'key': 'additionalName', 'writes': 'born_in[is=birth].additionalName'}, {'key': 'birthdate', 'writes': 'born_in[is=birth].startDate'}, {'key': 'familyName', 'writes': 'born_in[is=birth].familyName'}, {'key': 'gender', 'writes': 'born_in[is=birth].gender'}, {'key': 'givenName', 'writes': 'born_in[is=birth].givenName'}, {'key': 'honorificPrefix', 'writes': 'born_in[is=birth].honorificPrefix'}, {'key': 'honorificSuffix', 'writes': 'born_in[is=birth].honorificSuffix'}, {'key': 'legalName', 'writes': 'born_in[is=birth].legalName'}, {'key': 'maidenName', 'writes': 'born_in[is=birth].maidenName'}, {'key': 'nameOrder', 'writes': 'born_in[is=birth].nameOrder'}, {'key': 'nickname', 'writes': 'born_in[is=birth].nickname'}, {'key': 'phoneticFamilyName', 'writes': 'born_in[is=birth].phoneticFamilyName'}, {'key': 'phoneticGivenName', 'writes': 'born_in[is=birth].phoneticGivenName'}, {'key': 'sortAs', 'writes': 'born_in[is=birth].sortAs'}], 'also': ['actor'], 'identity_any': ['url'], 'display': {'subtitle': 'about', 'image': 'image', 'body': 'notes', 'highlights': ['birthdate', 'gender']}, 'groups': [{'name': 'Name', 'fields': ['givenName', 'additionalName', 'familyName', 'nickname', 'legalName', 'maidenName']}, {'name': 'Personal', 'fields': ['birthdate', 'gender', 'current_residence', 'current_role']}, {'name': 'About', 'fields': ['about', 'notes', 'url']}], 'prior_art': [{'source': 'schema.org/Person', 'url': 'https://schema.org/Person', 'notes': "Our givenName / familyName / additionalName / honorificPrefix / honorificSuffix live on `birth.yaml` (and `transition.yaml`), not on the person node itself — schema.org's `birthDate` lives on the `--born_in--> birth { startDate }` relationship per rule 1. We diverge by modeling accounts[] as a first-class relation rather than sameAs URLs."}, {'source': 'vCard 4.0 (RFC 6350) §6.2.2 N property + §5.9 SORT-AS', 'url': 'https://datatracker.ietf.org/doc/html/rfc6350#section-6.2.2', 'notes': "The N property is `family;given;additional;prefixes;suffixes`, each comma-multi-valued. Round-trips exactly through the birth event's structured name fields."}, {'source': 'W3C i18n — Personal names around the world', 'url': 'https://www.w3.org/International/questions/qa-personal-names', 'notes': 'Canonical reference for why "first/last" is a Western bias. CJK names put family first. Spanish uses two surnames. Icelandic uses patronymics without family names. The birth event\'s `nameOrder` field captures the rendering rule; structured fields stay neutral.'}, {'source': 'FOAF (Friend of a Friend)', 'url': 'http://xmlns.com/foaf/spec/', 'notes': 'Original social-graph vocabulary. Largely superseded by schema.org but still a reference for account-centric modeling.'}]},
    'persona': {'name': 'persona', 'plural': 'personas', 'description': 'An archetype of an audience segment — a named, hypothetical user that', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'goals', 'ty': 'stringlist'}, {'name': 'headline', 'ty': 'string'}, {'name': 'painPoints', 'ty': 'stringlist'}, {'name': 'quote', 'ty': 'text'}, {'name': 'reachesFor', 'ty': 'text'}, {'name': 'who', 'ty': 'text'}], 'display': {'subtitle': 'headline', 'body': 'who', 'highlights': ['reachesFor', 'quote']}, 'prior_art': [{'source': 'Alan Cooper, "The Inmates Are Running the Asylum" (1999)', 'url': 'https://www.nngroup.com/articles/persona/', 'notes': 'Origin of the persona method — "a precise definition of our user and what he wishes to accomplish"; a hypothetical archetype, not a real person. Maps to role + who + goals + quote.'}, {'source': 'schema.org/PeopleAudience', 'url': 'https://schema.org/PeopleAudience', 'notes': 'A persona is a narrative archetype OF an audience; it specializes Audience (audienceType) but adds goals/quote that schema.org lacks — and is firmly distinct from `person` (a real human).'}, {'source': 'Nielsen Norman Group — personas', 'url': 'https://www.nngroup.com/articles/persona/', 'notes': 'Canonical UX template — role + goals + pain points + quote, grounded in field research.'}]},
    'place': {'name': 'place', 'plural': 'places', 'description': 'A physical location — address, building, city, or point of interest.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'accuracy', 'ty': 'string'}, {'name': 'businessStatus', 'ty': 'string'}, {'name': 'categories', 'ty': 'stringlist'}, {'name': 'city', 'ty': 'string'}, {'name': 'closedMessage', 'ty': 'string'}, {'name': 'country', 'ty': 'string'}, {'name': 'countryCode', 'ty': 'string'}, {'name': 'district', 'ty': 'string'}, {'name': 'eta', 'ty': 'string'}, {'name': 'featureType', 'ty': 'string'}, {'name': 'fullAddress', 'ty': 'string'}, {'name': 'googlePlaceId', 'ty': 'string'}, {'name': 'hours', 'ty': 'json'}, {'name': 'isOrderable', 'ty': 'boolean'}, {'name': 'latitude', 'ty': 'number'}, {'name': 'locality', 'ty': 'string'}, {'name': 'longitude', 'ty': 'number'}, {'name': 'mapboxId', 'ty': 'string'}, {'name': 'neighborhood', 'ty': 'string'}, {'name': 'phone', 'ty': 'string'}, {'name': 'placeFormatted', 'ty': 'string'}, {'name': 'postalCode', 'ty': 'string'}, {'name': 'priceLevel', 'ty': 'string'}, {'name': 'productCount', 'ty': 'integer'}, {'name': 'rating', 'ty': 'number'}, {'name': 'region', 'ty': 'string'}, {'name': 'reviewCount', 'ty': 'integer'}, {'name': 'street', 'ty': 'string'}, {'name': 'streetNumber', 'ty': 'string'}, {'name': 'timezone', 'ty': 'string'}, {'name': 'website', 'ty': 'url'}, {'name': 'wikidataId', 'ty': 'string'}], 'identity_any': ['googlePlaceId', 'mapboxId'], 'display': {'subtitle': 'featureType', 'image': 'image', 'body': 'fullAddress', 'highlights': ['city', 'country', 'rating']}, 'prior_art': [{'source': 'schema.org/Place + PostalAddress', 'url': 'https://schema.org/Place', 'notes': 'Our latitude/longitude = geo.latitude/longitude; street/city/region/postalCode/countryCode map to PostalAddress streetAddress/addressLocality/addressRegion/postalCode/addressCountry; hours ≈ openingHoursSpecification; rating/reviewCount ≈ aggregateRating.'}, {'source': 'Google Places API (Place resource)', 'url': 'https://developers.google.com/maps/documentation/places/web-service/reference/rest/v1/places', 'notes': 'Practical POI schema. Our googlePlaceId = id; featureType/categories ≈ types/primaryType; businessStatus, priceLevel, rating match directly.'}, {'source': 'GeoJSON (RFC 7946) + ISO 3166-1', 'url': 'https://datatracker.ietf.org/doc/html/rfc7946', 'notes': 'Our latitude/longitude are a GeoJSON Point [lon, lat]; countryCode follows ISO 3166-1 alpha-2.'}]},
    'playlist': {'name': 'playlist', 'plural': 'playlists', 'description': 'A video playlist. Playlists are lists that contain videos instead of products.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'arrangement', 'ty': 'string'}, {'name': 'default_view', 'ty': 'string'}, {'name': 'icon_size', 'ty': 'integer'}, {'name': 'isDefault', 'ty': 'boolean'}, {'name': 'isPublic', 'ty': 'boolean'}, {'name': 'itemCount', 'ty': 'integer'}, {'name': 'listId', 'ty': 'string'}, {'name': 'listType', 'ty': 'string'}, {'name': 'member_shape', 'ty': 'string'}, {'name': 'ordering_mode', 'ty': 'string'}, {'name': 'path', 'ty': 'string'}, {'name': 'privacy', 'ty': 'string'}, {'name': 'sort_by', 'ty': 'string'}], 'also': ['list'], 'display': {'subtitle': 'text'}, 'prior_art': [{'source': 'schema.org/MusicPlaylist / ItemList', 'url': 'https://schema.org/MusicPlaylist', 'notes': 'Our contains(video[]) ≈ track/itemListElement. We generalize beyond music to any ordered media list.'}, {'source': 'YouTube Data API — Playlist', 'url': 'https://developers.google.com/youtube/v3/docs/playlists', 'notes': 'Practical source. Playlist = ordered Video collection — inherits list identity semantics.'}]},
    'podcast': {'name': 'podcast', 'plural': 'podcasts', 'description': "A podcast series. Contains episodes. Not the audio itself — that's on the episode.", 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'feedUrl', 'ty': 'url'}], 'identity': ['at', 'id'], 'display': {'subtitle': 'host'}, 'prior_art': [{'source': 'RSS 2.0 (feed + channel)', 'url': 'https://www.rssboard.org/rss-specification', 'notes': "Our feedUrl is a canonical RSS feed URL; episodes relation ≈ channel's item elements."}, {'source': 'Apple Podcasts RSS extensions (itunes:*)', 'url': 'https://help.apple.com/itc/podcasts_connect/#/itcb54353390', 'notes': 'De-facto standard. Our host[] ≈ itunes:author; our series-episode hierarchy aligns with itunes:episode/itunes:season.'}, {'source': 'Podcast Namespace (podcast:*)', 'url': 'https://podcastindex.org/namespace/1.0', 'notes': 'Modern open extension. podcast:person covers guests/hosts; podcast:transcript covers our transcribe relation.'}]},
    'post': {'name': 'post', 'plural': 'posts', 'description': 'A piece of published content — a Reddit submission, HN story, YouTube upload,', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'commentCount', 'ty': 'integer'}, {'name': 'community', 'ty': 'string'}, {'name': 'externalUrl', 'ty': 'url'}, {'name': 'postType', 'ty': 'string'}, {'name': 'score', 'ty': 'integer'}], 'identity': ['at', 'id'], 'display': {'subtitle': 'author'}, 'prior_art': [{'source': 'ActivityStreams 2.0 (Note/Article + Create)', 'url': 'https://www.w3.org/TR/activitystreams-vocabulary/', 'notes': 'Fediverse post model. Our postedBy ≈ actor/attributedTo; publish(community) ≈ audience/to; repliesTo/replies ≈ inReplyTo/replies; media/attachment ≈ attachment.'}, {'source': 'OpenGraph protocol', 'url': 'https://ogp.me/', 'notes': 'How posts surface when linked. Our externalUrl + media[] correspond to og:url and og:image/og:video; postType loosely parallels og:type (article, video).'}, {'source': 'ATProto app.bsky.feed.post', 'url': 'https://atproto.com/lexicons/app-bsky-feed', 'notes': 'Modern practical lexicon. Our repliesTo ≈ reply.parent; media ≈ embed.images; externalUrl ≈ embed.external.'}]},
    'practice': {'name': 'practice', 'plural': 'practices', 'description': 'A field of practice or study — a discipline a person practices, or the', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'aliases', 'ty': 'stringlist'}, {'name': 'code', 'ty': 'string'}, {'name': 'codeSystem', 'ty': 'string'}, {'name': 'description', 'ty': 'text'}], 'display': {'subtitle': 'parent'}, 'prior_art': [{'source': 'NUCC Health Care Provider Taxonomy', 'url': 'https://www.nucc.org/index.php/code-sets-mainmenu-41/provider-taxonomy-mainmenu-40', 'notes': 'US medical-specialty code set — 3 levels (Grouping / Classification / Specialization), 10-char alphanumeric codes. The source for codeSystem=NUCC and for the parent-link hierarchy.'}, {'source': 'Standard Occupational Classification (SOC) / O*NET-SOC', 'url': 'https://www.bls.gov/soc/', 'notes': 'US occupational taxonomy spanning every profession — 4 levels (Major / Minor / Broad / Detailed). codeSystem=SOC.'}, {'source': 'ISCED Fields of Education and Training 2013 (ISCED-F)', 'url': 'https://esco.ec.europa.eu/en/about-esco/escopedia/escopedia/international-standard-classification-education-fields-education-and', 'notes': "UNESCO field-of-study taxonomy — 3 levels (Broad / Narrow / Detailed). The field-of-study side, for a qualification's `field`."}, {'source': 'schema.org CategoryCode / occupationalCategory', 'url': 'https://schema.org/occupationalCategory', 'notes': 'schema.org has no dedicated discipline type — only the pluggable CategoryCode (codeValue + inCodeSet). Confirms code + codeSystem as a loose optional pair, not a hard taxonomy dependency.'}]},
    'principle': {'name': 'principle', 'plural': 'principles', 'description': 'A guiding bright-line — a value or rule used to judge edge cases. Universal:', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'domain', 'ty': 'string'}, {'name': 'rationale', 'ty': 'text'}, {'name': 'statement', 'ty': 'text'}, {'name': 'status', 'ty': 'string'}], 'display': {'subtitle': 'domain', 'body': 'rationale', 'highlights': ['statement', 'status']}, 'prior_art': [{'source': 'principles.design', 'url': 'https://principles.design/', 'notes': '1600+ principles modeled as name + statement + elaboration, grouped into named collections → name / statement / rationale.'}, {'source': 'MADR (Markdown ADR) — decision drivers', 'url': 'https://adr.github.io/madr/', 'notes': 'Decision drivers are principles applied to a choice; the status enum (proposed/accepted/deprecated/superseded) → status + supersedes.'}, {'source': 'GOV.UK Design Principles', 'url': 'https://www.gov.uk/guidance/government-design-principles', 'notes': 'Canonical 10-principle collection — each principle is an imperative statement + worked examples.'}]},
    'product': {'name': 'product', 'plural': 'products', 'description': 'A purchasable item OR an identifiable product released into the world.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'aisle', 'ty': 'string'}, {'name': 'availability', 'ty': 'string'}, {'name': 'barcode', 'ty': 'string'}, {'name': 'calories', 'ty': 'number'}, {'name': 'categories', 'ty': 'stringlist'}, {'name': 'category', 'ty': 'string'}, {'name': 'currency', 'ty': 'string'}, {'name': 'customizationGroups', 'ty': 'json'}, {'name': 'department', 'ty': 'string'}, {'name': 'images', 'ty': 'json'}, {'name': 'novaGroup', 'ty': 'integer'}, {'name': 'nutritionScore', 'ty': 'string'}, {'name': 'originalPrice', 'ty': 'string'}, {'name': 'originalPriceAmount', 'ty': 'number'}, {'name': 'price', 'ty': 'string'}, {'name': 'priceAmount', 'ty': 'number'}, {'name': 'quantity', 'ty': 'integer'}, {'name': 'servingSize', 'ty': 'string'}, {'name': 'sku', 'ty': 'string'}, {'name': 'soldByWeight', 'ty': 'boolean'}, {'name': 'weight', 'ty': 'string'}, {'name': 'weightUnit', 'ty': 'string'}, {'name': 'weightValue', 'ty': 'number'}], 'identity_any': ['url'], 'display': {'subtitle': 'brand'}, 'prior_art': [{'source': 'schema.org/Product + Offer', 'url': 'https://schema.org/Product', 'notes': 'Product on schema.org, price/priceAmount/currency/availability on nested Offer. Our sku/barcode map to sku/gtin13/gtin12; brand/manufacturer match directly. schema.org has `releaseDate` on Product (mirrors our `released`) but no formalized end-of-life property.'}, {'source': 'Wikidata P2669 (discontinued date)', 'url': 'https://www.wikidata.org/wiki/Property:P2669', 'notes': 'Wikidata\'s canonical "discontinued date" property — broadly used across Wikidata\'s product entities (software, hardware, vehicles, consumer goods) with consistent semantics ("date when a product ceased to be manufactured, supported, or available"). Our `discontinued` field aligns directly. Wikidata P577 (publication date) similarly aligns with our `released`.'}, {'source': 'schema.org/CreativeWork (creator, isBasedOn)', 'url': 'https://schema.org/CreativeWork', 'notes': 'Our `creator: actor[]` mirrors schema.org/creator (Person|Organization). Our `inspiredBy: product[]` maps to schema.org/isBasedOn (CreativeWork derivation/credit link); we keep the more readable name and broaden the target to any product so non-CreativeWork lineages (one aircraft type inspired by another, one OS inspired by another) work the same way.'}, {'source': 'GS1 GTIN (UPC/EAN)', 'url': 'https://www.gs1.org/standards/id-keys/gtin', 'notes': "Canonical barcode standard. Our barcode field is a GTIN-8/12/13/14; GS1 also underlies schema.org's gtin* properties."}, {'source': 'Open Food Facts API', 'url': 'https://openfoodfacts.github.io/openfoodfacts-server/api/', 'notes': 'Best practical source for food attributes. Our nutritionScore/novaGroup/calories/servingSize mirror nutriscore_grade/nova_group/nutriments.energy-kcal/serving_size.'}]},
    'project': {'name': 'project', 'plural': 'projects', 'description': 'A project that groups tasks. Tasks belong to projects.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'color', 'ty': 'string'}, {'name': 'parentId', 'ty': 'string'}, {'name': 'state', 'ty': 'string'}], 'identity': ['at', 'id'], 'display': {'subtitle': 'state'}, 'prior_art': [{'source': 'Linear API — Project', 'url': 'https://developers.linear.app/docs/graphql/working-with-the-graphql-api', 'notes': "Our state/color come directly from Linear's Project model."}, {'source': 'GitHub Projects (v2)', 'url': 'https://docs.github.com/en/graphql/reference/objects#projectv2', 'notes': 'Canonical open-source project-board model. state ≈ ProjectV2SingleSelectFieldOption; color is per-field metadata.'}, {'source': 'schema.org/Project', 'url': 'https://schema.org/Project', 'notes': 'Generic project-as-effort type. Thinner than the practical APIs; mainly useful for outbound JSON-LD.'}]},
    'protocol': {'name': 'protocol', 'plural': 'protocols', 'description': 'A protocol or technical spec — git, bitcoin, ssh, smtp, oauth, etc.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'homepage', 'ty': 'url'}, {'name': 'rfc', 'ty': 'string'}, {'name': 'wikidataId', 'ty': 'string'}], 'identity': ['name'], 'display': {'subtitle': 'name'}, 'prior_art': [{'source': 'schema.org/CreativeWork', 'url': 'https://schema.org/CreativeWork', 'notes': 'Closest match in schema.org — protocols are creative works in the broadest sense. We narrow to protocols and technical specifications used as identity namespaces.'}, {'source': 'Wikidata (Communication protocol, Q15836568)', 'url': 'https://www.wikidata.org/wiki/Q15836568', 'notes': 'wikidataId enables cross-reference for dedupe across other knowledge graphs. Most well-known protocols have Q-IDs.'}, {'source': 'IANA Protocol Registry', 'url': 'https://www.iana.org/protocols', 'notes': 'Authoritative registry for many protocols. Our `name` aligns with IANA protocol slugs where applicable.'}]},
    'qualification': {'name': 'qualification', 'plural': 'qualifications', 'description': 'An earned qualification — a degree, professional license, board', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'category', 'ty': 'string'}, {'name': 'identifier', 'ty': 'string'}, {'name': 'level', 'ty': 'string'}, {'name': 'renewalPeriod', 'ty': 'string'}, {'name': 'status', 'ty': 'string'}, {'name': 'validIn', 'ty': 'string'}, {'name': 'verificationUrl', 'ty': 'url'}], 'identity_any': ['identifier'], 'display': {'subtitle': 'category', 'highlights': ['identifier', 'validIn', 'granted_by']}, 'prior_art': [{'source': 'schema.org EducationalOccupationalCredential', 'url': 'https://schema.org/EducationalOccupationalCredential', 'notes': 'Single credential class with a credentialCategory discriminator; recognizedBy, validFor, validIn, educationalLevel. Person.hasCredential links the holder — our `held_by` link.'}, {'source': 'CTDL — Credential Transparency Description Language (Credential Engine)', 'url': 'https://credreg.net/ctdl/terms/CredentialType', 'notes': 'The most thorough credential ontology — a Credential superclass with ~40 subtypes and four distinct org roles (ownedBy / offeredBy vs accreditedBy / regulatedBy / recognizedBy). The source for splitting `granted_by` from `governed_by`; we collapse the regulator family into one link — four roles is over-modeled for a personal graph.'}, {'source': 'W3C Verifiable Credentials Data Model 2.0', 'url': 'https://www.w3.org/TR/vc-data-model-2.0/', 'notes': 'Separates the issuer + validFrom / validUntil (the issuing act) from credentialSubject (the claim); credentialStatus models revocation — our `status` covers revoked / suspended, which schema.org omits.'}, {'source': 'Open Badges 3.0 (1EdTech)', 'url': 'https://www.imsglobal.org/spec/ob/v3p0/impl', 'notes': 'Achievement.achievementType enum (Certificate, Certification, Degree, License, Badge, MicroCredential) — confirms one shape plus a category enum across every credential kind.'}, {'source': 'LinkedIn Licenses & Certifications', 'url': 'https://www.linkedin.com/help/linkedin/answer/a567169', 'notes': 'Real-world minimal field set — name, issuing organization, issue date, expiration date, credential ID, credential URL. Its Education / Licenses UI split is the seam this shape unifies.'}]},
    'quantity-kind': {'name': 'quantity-kind', 'plural': 'quantity-kinds', 'description': 'A quantity kind — WHAT is being measured, semantically. "Mass', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'key', 'ty': 'string', 'required': True}, {'name': 'label', 'ty': 'string'}], 'identity': ['key'], 'display': {'subtitle': 'label'}, 'prior_art': [{'source': 'ISO 80000-1 — kind of quantity', 'url': 'https://www.iso.org/standard/76921.html', 'notes': 'ISO 80000 makes "kind of quantity" a rigorous first-class notion, distinct from dimension — quantities of the same dimension are not necessarily of the same kind.'}, {'source': 'QUDT — QuantityKind', 'url': 'https://www.qudt.org/doc/DOC_SCHEMA-QUDT.html', 'notes': "qudt:QuantityKind is exactly this layer. Its hasDimensionVector property corresponds to our `dimension` link; QUDT's broader/ narrower kind hierarchy corresponds to our `parent` link."}]},
    'quote': {'name': 'quote', 'plural': 'quotes', 'description': 'A notable quote. Attribution is a graph relationship, not a field —', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'context', 'ty': 'string'}, {'name': 'year', 'ty': 'integer'}], 'display': {'subtitle': 'year'}, 'prior_art': [{'source': 'schema.org/Quotation', 'url': 'https://schema.org/Quotation', 'notes': 'Our context ≈ about; year ≈ datePublished. schema.org models spokenByCharacter/creator — we model attribution via graph links instead.'}, {'source': 'Wikiquote data model', 'url': 'https://en.wikiquote.org/wiki/Help:Sources', 'notes': "Practical canonical quote source. Our provenance-via-links (document --contains--> quote --attributedTo--> person) matches Wikiquote's source-citation discipline."}]},
    'repository': {'name': 'repository', 'plural': 'repositories', 'description': 'A source code repository.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'defaultBranch', 'ty': 'string'}, {'name': 'forks', 'ty': 'integer'}, {'name': 'isArchived', 'ty': 'boolean'}, {'name': 'isPrivate', 'ty': 'boolean'}, {'name': 'language', 'ty': 'string'}, {'name': 'license', 'ty': 'string'}, {'name': 'openIssues', 'ty': 'integer'}, {'name': 'size', 'ty': 'integer'}, {'name': 'stars', 'ty': 'integer'}, {'name': 'topics', 'ty': 'stringlist'}], 'identity_any': ['path', 'url'], 'display': {'subtitle': 'language'}, 'prior_art': [{'source': 'Git internals + Git refs', 'url': 'https://git-scm.com/book/en/v2/Git-Internals-Git-References', 'notes': 'Our defaultBranch is a Git ref (refs/heads/main); forkedFrom is explicit in our model vs. implicit in Git (recorded only by forges).'}, {'source': 'GitHub REST API — Repository', 'url': 'https://docs.github.com/en/rest/repos/repos', 'notes': 'Direct source. Our stars/forks/openIssues/topics/defaultBranch/ license/size/isArchived/isPrivate all come from the GitHub Repository resource.'}, {'source': 'SPDX License List', 'url': 'https://spdx.org/licenses/', 'notes': 'Our license values are SPDX identifiers (MIT, Apache-2.0, GPL-3.0-or-later).'}]},
    'reservation': {'name': 'reservation', 'plural': 'reservations', 'description': 'A forward commitment to a future thing — a flight booking, a hotel', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'allDay', 'ty': 'boolean'}, {'name': 'availableActions', 'ty': 'stringlist'}, {'name': 'baseAmount', 'ty': 'number'}, {'name': 'bookingTime', 'ty': 'datetime'}, {'name': 'bookingType', 'ty': 'string'}, {'name': 'checkinUrl', 'ty': 'url'}, {'name': 'conditions', 'ty': 'json'}, {'name': 'currency', 'ty': 'string'}, {'name': 'currentUrl', 'ty': 'string'}, {'name': 'dateUpdated', 'ty': 'datetime'}, {'name': 'distinctId', 'ty': 'string'}, {'name': 'endDate', 'ty': 'datetime'}, {'name': 'endTime', 'ty': 'datetime'}, {'name': 'icalUid', 'ty': 'string'}, {'name': 'modifiedTime', 'ty': 'datetime'}, {'name': 'partySize', 'ty': 'integer'}, {'name': 'properties', 'ty': 'json'}, {'name': 'recurrence', 'ty': 'stringlist'}, {'name': 'reservationId', 'ty': 'string', 'required': True}, {'name': 'reservationType', 'ty': 'string'}, {'name': 'showAs', 'ty': 'string'}, {'name': 'sourceTitle', 'ty': 'string'}, {'name': 'sourceUrl', 'ty': 'url'}, {'name': 'startDate', 'ty': 'datetime'}, {'name': 'startTime', 'ty': 'datetime'}, {'name': 'status', 'ty': 'string'}, {'name': 'taxAmount', 'ty': 'number'}, {'name': 'timezone', 'ty': 'string'}, {'name': 'totalAmount', 'ty': 'number'}, {'name': 'visibility', 'ty': 'string'}, {'name': 'voidWindowEndsAt', 'ty': 'datetime'}], 'also': ['event'], 'identity': ['at', 'reservationId'], 'display': {'subtitle': 'reservationType', 'highlights': ['startDate', 'endDate', 'location']}, 'prior_art': [{'source': 'schema.org/Reservation', 'url': 'https://schema.org/Reservation', 'notes': 'Base vocabulary: reservationFor, reservationId, reservationStatus, reservedTicket, underName, bookingTime, modifiedTime, totalPrice, priceCurrency. We fold FlightReservation / LodgingReservation / FoodEstablishmentReservation into a single shape with a reservationType discriminator (AgentOS convention — see `trip.tripType`, `event.eventType`). Flight-specific fields (boardingGroup, seat) live on pass, not here.'}, {'source': 'schema.org/ReservationStatusType', 'url': 'https://schema.org/ReservationStatusType', 'notes': "Extended beyond schema.org's ConfirmedCancelledHoldPending set to add `no_show` and `completed` — values that matter for post-hoc reasoning but schema.org lacks."}, {'source': 'Duffel Orders API', 'url': 'https://duffel.com/docs/api/v2/orders', 'notes': 'Canonical flight-booking top-level entity. Our `reservationId` = booking_reference; `availableActions` = available_actions; `voidWindowEndsAt` = void_window_ends_at; `conditions` = conditions (change_before_departure, refund_before_departure). Duffel names the entity `Order`; we chose `reservation` to free up `order` for pure-commerce semantics.'}, {'source': 'IATA NDC OrderViewRS', 'url': 'https://www.iata.org/en/programs/airline-distribution/retailing/ndc/', 'notes': 'NDC normalizes passengers to a top-level PaxList referenced by ID. Our graph gets the same effect with `passengers: person[]` — people are first-class nodes and the same `person` can appear on many reservations. Services (seat, baggage, meal) live on `pass`.'}, {'source': 'ActivityStreams 2.0 (Invite / Accept / Leave / Reject)', 'url': 'https://www.w3.org/TR/activitystreams-vocabulary/', 'notes': 'Commitment lifecycle is an append-only stream of activities (booked, held, checked_in, rebooked, cancelled) rather than a single lossy enum. We use `status` for the snapshot and rely on back-links from `activity` nodes for the history — the same pattern FEP-8a8e recommends for ActivityPub event-side state.'}, {'source': 'FEP-8a8e Event interop', 'url': 'https://w3id.org/fep/8a8e', 'notes': 'Splits supply-side status (on the event/flight) from demand-side status (on the attendee/passenger). We mirror this by keeping `status` on reservation (passenger-side) separate from any cancellation/delay state on the `flight` or `trip` itself.'}, {'source': 'Valueflows / REA — Commitment', 'url': 'https://www.valueflo.ws/concepts/flows/', 'notes': 'REA accounting framing: a reservation IS a commitment with provider, receiver, resourceConformsTo, quantity, and time window. Useful lens for future extension (hotel nights, car rental days).'}]},
    'result': {'name': 'result', 'plural': 'results', 'description': 'A search result — a pointer to something found. Not the thing itself.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'community', 'ty': 'string'}, {'name': 'externalUrl', 'ty': 'url'}, {'name': 'favicon', 'ty': 'url'}, {'name': 'indexedAt', 'ty': 'datetime'}, {'name': 'postId', 'ty': 'string'}, {'name': 'resultType', 'ty': 'string'}, {'name': 'score', 'ty': 'integer'}, {'name': 'similarity', 'ty': 'number'}], 'display': {'subtitle': 'url'}, 'prior_art': [{'source': 'OpenSearch Description Document', 'url': 'https://github.com/dewitt/opensearch/blob/master/opensearch-1-1-draft-6.md', 'notes': "Result-pointer model: each hit has a URL + metadata. Our resultType ≈ Url template's type attribute."}, {'source': 'Web Search API conventions (Brave/Bing)', 'url': 'https://api.search.brave.com/app/documentation/web-search/get-started', 'notes': 'Practical source. Our indexedAt/resultType align with common fields across Brave, Bing, and Exa web APIs.'}]},
    'review': {'name': 'review', 'plural': 'reviews', 'description': 'A user review of a product. Reviews are also posts, so they carry engagement metrics.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'commentCount', 'ty': 'integer'}, {'name': 'community', 'ty': 'string'}, {'name': 'externalUrl', 'ty': 'url'}, {'name': 'isVerified', 'ty': 'boolean'}, {'name': 'postType', 'ty': 'string'}, {'name': 'rating', 'ty': 'number'}, {'name': 'ratingMax', 'ty': 'number'}, {'name': 'score', 'ty': 'integer'}, {'name': 'tags', 'ty': 'stringlist'}], 'also': ['post'], 'display': {'subtitle': 'author'}, 'prior_art': [{'source': 'schema.org/Review', 'url': 'https://schema.org/Review', 'notes': 'Our rating ≈ reviewRating.ratingValue; ratingMax ≈ bestRating; reviews = itemReviewed; isVerified has no direct property (extension).'}, {'source': 'schema.org/AggregateRating', 'url': 'https://schema.org/AggregateRating', 'notes': 'For product review aggregates. Our rating/ratingMax map to ratingValue/bestRating; reviewCount is inherited when computed.'}]},
    'role': {'name': 'role', 'plural': 'roles', 'description': "A person's position at an organization (job title, board seat, etc.).", 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'allDay', 'ty': 'boolean'}, {'name': 'currentUrl', 'ty': 'string'}, {'name': 'dateUpdated', 'ty': 'datetime'}, {'name': 'department', 'ty': 'string'}, {'name': 'distinctId', 'ty': 'string'}, {'name': 'endDate', 'ty': 'datetime'}, {'name': 'icalUid', 'ty': 'string'}, {'name': 'properties', 'ty': 'json'}, {'name': 'recurrence', 'ty': 'stringlist'}, {'name': 'roleType', 'ty': 'string'}, {'name': 'showAs', 'ty': 'string'}, {'name': 'sourceTitle', 'ty': 'string'}, {'name': 'sourceUrl', 'ty': 'url'}, {'name': 'startDate', 'ty': 'datetime'}, {'name': 'status', 'ty': 'string'}, {'name': 'timezone', 'ty': 'string'}, {'name': 'title', 'ty': 'string'}, {'name': 'visibility', 'ty': 'string'}], 'also': ['event'], 'display': {'subtitle': 'name', 'highlights': ['startDate', 'endDate', 'location']}, 'prior_art': [{'source': 'schema.org/Role + OrganizationRole', 'url': 'https://schema.org/OrganizationRole', 'notes': "Our title = roleName; startDate/endDate match; department ≈ name of a subOrganization; person/organization = Role's nested pattern."}, {'source': 'FOAF + Bio vocabularies (position)', 'url': 'http://vocab.org/bio/0.1/.html', 'notes': 'Period-of-employment modeling. Our startDate/endDate ≈ bio:date; roleType has no FOAF peer.'}]},
    'seatmap': {'name': 'seatmap', 'plural': 'seatmaps', 'description': 'A seat map for a specific flight + cabin, returned by an airline app.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'aircraftCode', 'ty': 'string'}, {'name': 'availableSeats', 'ty': 'integer'}, {'name': 'basicEconomyLocked', 'ty': 'boolean'}, {'name': 'cabins', 'ty': 'json'}, {'name': 'classOfService', 'ty': 'string'}, {'name': 'destination', 'ty': 'string'}, {'name': 'fareBasisCode', 'ty': 'string'}, {'name': 'flightNumber', 'ty': 'string'}, {'name': 'hasExitRow', 'ty': 'boolean'}, {'name': 'hasFreeSeats', 'ty': 'boolean'}, {'name': 'hasPaidSeats', 'ty': 'boolean'}, {'name': 'origin', 'ty': 'string'}, {'name': 'tiers', 'ty': 'json'}, {'name': 'totalSeats', 'ty': 'integer'}], 'identity': ['id'], 'display': {'title': 'flightNumber'}},
    'service': {'name': 'service', 'plural': 'services', 'description': 'A service — a named interface the engine brokers between strangers.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'description', 'ty': 'text'}, {'name': 'params', 'ty': 'json'}, {'name': 'returns', 'ty': 'string'}], 'identity': ['id'], 'display': {'subtitle': 'description'}, 'prior_art': [{'source': 'Debian alternatives system (update-alternatives)', 'url': 'https://wiki.debian.org/DebianAlternatives', 'notes': 'A generic name (editor) resolves to one of several registered providers via a per-name symlink the admin can repoint. Our service id ≈ the generic name; defaults_to ≈ the symlink.'}, {'source': 'Windows XP — Set Program Access and Defaults', 'url': 'https://learn.microsoft.com/en-us/windows/win32/shell/default-programs', 'notes': 'The OS-level "which program answers this kind of request" surface. Our defaults_to link is that choice as graph state.'}, {'source': 'Android Intents (action + default app)', 'url': 'https://developer.android.com/guide/components/intents-filters', 'notes': 'Apps declare which actions they answer; the user picks a default per action. provided_by ≈ intent-filter; defaults_to ≈ the user\'s "always" choice.'}]},
    'settings': {'name': 'settings', 'plural': 'settings', 'description': "An AgentOS settings node — the user's portable configuration store,", 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}], 'display': {'subtitle': 'name'}, 'prior_art': [{'source': 'macOS ~/Library/Application Support + Preferences', 'url': 'https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/MacOSXDirectories/MacOSXDirectories.html', 'notes': "Direct precedent. macOS keeps per-user, per-app configuration in the user's home Library — portable with the home directory, one subdirectory per app. Our parent settings node mirrors Preferences (the OS defaults domain); each `--configures-->` app node mirrors one Application Support/<App> directory. We diverge by living in the graph (queryable, cascade-resolved) rather than plist files on disk."}, {'source': 'XDG Base Directory ($XDG_CONFIG_HOME)', 'url': 'https://specifications.freedesktop.org/basedir-spec/latest/', 'notes': 'The Linux convention: user config under ~/.config/<app>, machine state kept separate. Same person-vs-machine seam we draw between this home settings store and the System-resident seat.'}]},
    'shape': {'name': 'shape', 'plural': 'shapes', 'description': 'A shape definition - the ontology node that describes a node type.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'also', 'ty': 'stringlist'}, {'name': 'derived', 'ty': 'json'}, {'name': 'description', 'ty': 'text'}, {'name': 'display', 'ty': 'json'}, {'name': 'fields', 'ty': 'json'}, {'name': 'groups', 'ty': 'json'}, {'name': 'icon', 'ty': 'string'}, {'name': 'identity', 'ty': 'stringlist'}, {'name': 'identity_any', 'ty': 'stringlist'}, {'name': 'in', 'ty': 'json'}, {'name': 'out', 'ty': 'json'}, {'name': 'plural', 'ty': 'string'}, {'name': 'prefsSchemas', 'ty': 'json'}, {'name': 'prior_art', 'ty': 'json'}, {'name': 'shortcuts', 'ty': 'json'}], 'identity': ['name'], 'display': {'subtitle': 'description', 'body': 'description', 'highlights': ['plural']}, 'groups': [{'name': 'Schema', 'fields': ['fields', 'out', 'in']}, {'name': 'Display', 'fields': ['display', 'groups']}, {'name': 'Identity', 'fields': ['identity', 'identity_any', 'also']}, {'name': 'Automation', 'fields': ['derived', 'shortcuts']}, {'name': 'Sources', 'fields': ['prior_art']}, {'name': 'Preferences', 'fields': ['prefsSchemas']}], 'prior_art': [{'source': 'JSON Schema', 'url': 'https://json-schema.org/', 'notes': 'Prior art for describing fields and JSON-shaped validation contracts. AgentOS keeps shape identity and graph relations first-class instead of flattening everything into one document schema.'}, {'source': 'W3C SHACL', 'url': 'https://www.w3.org/TR/shacl/', 'notes': 'Prior art for RDF graph shape constraints. AgentOS uses the same idea - graph data has shapes - but stores the shape definition as an inspectable node in the local graph.'}, {'source': 'RDF Schema', 'url': 'https://www.w3.org/TR/rdf-schema/', 'notes': 'Prior art for classes/properties as graph vocabulary. AgentOS shape nodes are the local, executable version of that vocabulary.'}]},
    'shelf': {'name': 'shelf', 'plural': 'shelves', 'description': 'A bookshelf. Shelves are lists that contain books instead of generic products.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'arrangement', 'ty': 'string'}, {'name': 'default_view', 'ty': 'string'}, {'name': 'icon_size', 'ty': 'integer'}, {'name': 'isDefault', 'ty': 'boolean'}, {'name': 'isExclusive', 'ty': 'boolean'}, {'name': 'isPublic', 'ty': 'boolean'}, {'name': 'itemCount', 'ty': 'integer'}, {'name': 'listId', 'ty': 'string'}, {'name': 'listType', 'ty': 'string'}, {'name': 'member_shape', 'ty': 'string'}, {'name': 'ordering_mode', 'ty': 'string'}, {'name': 'path', 'ty': 'string'}, {'name': 'privacy', 'ty': 'string'}, {'name': 'sort_by', 'ty': 'string'}], 'also': ['list'], 'display': {'subtitle': 'isExclusive'}, 'prior_art': [{'source': 'Goodreads API — Shelves', 'url': 'https://www.goodreads.com/api', 'notes': 'Direct source. Our isExclusive maps to Goodreads\' "exclusive shelves" (read, to-read, currently-reading).'}, {'source': 'schema.org/ItemList (bookshelf)', 'url': 'https://schema.org/ItemList', 'notes': 'Generic collection peer. contains(book[]) ≈ itemListElement.'}]},
    'software': {'name': 'software', 'plural': 'software', 'description': 'A software product — operating system, application, library, icon pack,', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'aisle', 'ty': 'string'}, {'name': 'applicationCategory', 'ty': 'string'}, {'name': 'availability', 'ty': 'string'}, {'name': 'barcode', 'ty': 'string'}, {'name': 'calories', 'ty': 'number'}, {'name': 'categories', 'ty': 'stringlist'}, {'name': 'category', 'ty': 'string'}, {'name': 'codename', 'ty': 'string'}, {'name': 'currency', 'ty': 'string'}, {'name': 'customizationGroups', 'ty': 'json'}, {'name': 'department', 'ty': 'string'}, {'name': 'images', 'ty': 'json'}, {'name': 'novaGroup', 'ty': 'integer'}, {'name': 'nutritionScore', 'ty': 'string'}, {'name': 'originalPrice', 'ty': 'string'}, {'name': 'originalPriceAmount', 'ty': 'number'}, {'name': 'price', 'ty': 'string'}, {'name': 'priceAmount', 'ty': 'number'}, {'name': 'quantity', 'ty': 'integer'}, {'name': 'runtimePlatform', 'ty': 'string'}, {'name': 'servingSize', 'ty': 'string'}, {'name': 'sku', 'ty': 'string'}, {'name': 'soldByWeight', 'ty': 'boolean'}, {'name': 'version', 'ty': 'string'}, {'name': 'weight', 'ty': 'string'}, {'name': 'weightUnit', 'ty': 'string'}, {'name': 'weightValue', 'ty': 'number'}], 'also': ['product'], 'identity_any': ['url'], 'display': {'subtitle': 'applicationCategory', 'highlights': ['version', 'runtimePlatform']}, 'prior_art': [{'source': 'schema.org/SoftwareApplication', 'url': 'https://schema.org/SoftwareApplication', 'notes': 'Our applicationCategory mirrors schema.org applicationCategory (free-form string, common values include "GameApplication", "BusinessApplication", "BrowserApplication"). Our version maps to softwareVersion; runtimePlatform maps to operatingSystem (the closest analog — schema.org uses `operatingSystem` to mean "which platform the software runs on", which matches our intent). Codename has no schema.org equivalent.'}, {'source': 'schema.org/SoftwareSourceCode', 'url': 'https://schema.org/SoftwareSourceCode', 'notes': "For libraries / open-source code (XP.css, 98.css), schema.org has a separate SoftwareSourceCode type with codeRepository / programmingLanguage fields. We keep one `software` shape and let the product's url field carry the repo URL when applicable."}, {'source': 'Wikidata Q7397 (software)', 'url': 'https://www.wikidata.org/wiki/Q7397', 'notes': 'Wikidata software entities use P348 (software version identifier), P178 (developer) ≈ our manufacturer/creator, P306 (operating system) ≈ our runtimePlatform, and P2669 (discontinued date) — inherited from product. Cross-reference identity rather than direct field alignment.'}]},
    'sound': {'name': 'sound', 'plural': 'sounds', 'description': 'An audio clip — startup chimes, error beeps, notification dings,', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'bitDepth', 'ty': 'integer'}, {'name': 'channels', 'ty': 'integer'}, {'name': 'copyrightYear', 'ty': 'integer'}, {'name': 'coverage', 'ty': 'string'}, {'name': 'dateCreated', 'ty': 'date'}, {'name': 'description', 'ty': 'string'}, {'name': 'durationMs', 'ty': 'integer'}, {'name': 'encoding', 'ty': 'string'}, {'name': 'filename', 'ty': 'string'}, {'name': 'format', 'ty': 'string'}, {'name': 'kind', 'ty': 'string'}, {'name': 'language', 'ty': 'string'}, {'name': 'license', 'ty': 'string'}, {'name': 'lineCount', 'ty': 'integer'}, {'name': 'mimeType', 'ty': 'string'}, {'name': 'path', 'ty': 'string'}, {'name': 'purpose', 'ty': 'string'}, {'name': 'sampleRate', 'ty': 'integer'}, {'name': 'sha', 'ty': 'string'}, {'name': 'size', 'ty': 'integer'}, {'name': 'tags', 'ty': 'stringlist'}], 'also': ['creative_work', 'file'], 'identity_any': ['sha', 'url'], 'display': {'subtitle': 'purpose', 'image': 'image', 'body': 'description', 'highlights': ['datePublished', 'published_by']}, 'prior_art': [{'source': 'schema.org/AudioObject', 'url': 'https://schema.org/AudioObject', 'notes': "Our durationMs ≈ duration (ISO 8601 period). Most metadata comes from creative_work via `also`; AudioObject's surface is sparse (contentUrl, encodingFormat, transcript)."}, {'source': 'ID3v2 (audio metadata in MP3)', 'url': 'https://id3.org/id3v2.4.0-structure', 'notes': 'TPE1=artist (author via creative_work); TALB=album; TIT2=title (name via creative_work); TYER=year (copyrightYear via creative_work); TCOP=copyright; TCOM=composer.'}, {'source': 'WAV LIST INFO chunks', 'url': 'https://www.recordingblogs.com/wiki/list-chunk-of-a-wave-file', 'notes': 'IART=artist; ICOP=copyright; ICRD=creation date; INAM=name; IGNR=genre. Inherited from creative_work where they apply.'}, {'source': 'Broadcast Wave Format (BWF) bext chunk', 'url': 'https://tech.ebu.ch/docs/tech/tech3285.pdf', 'notes': "BWF carries Originator (creator), OriginationDate, OriginatorReference — production-pipeline provenance for broadcast audio. Inherited via creative_work; AgentOS doesn't currently parse bext chunks."}]},
    'source': {'name': 'source', 'plural': 'sources', 'description': 'A content source — where apps, themes, shapes, and wallpapers live.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'address', 'ty': 'string', 'required': True}, {'name': 'description', 'ty': 'text'}, {'name': 'enabled', 'ty': 'boolean'}, {'name': 'lastSynced', 'ty': 'datetime'}, {'name': 'scanner', 'ty': 'string'}, {'name': 'sourceId', 'ty': 'string'}], 'identity': ['address'], 'display': {'subtitle': 'sourceId'}, 'prior_art': [{'source': 'Homebrew Taps', 'url': 'https://docs.brew.sh/Taps', 'notes': 'Direct precedent. Our sourceId/address match tap name/URL; our platform=agentos parallels tap formulae discovery.'}, {'source': 'Cydia / Sileo (APT repos for iOS)', 'url': 'https://wiki.theapebox.com/index.php/Package_Management', 'notes': 'Namespaced third-party source model. Our sourceId prefix is the Cydia repo-namespace pattern.'}, {'source': 'Debian APT sources.list', 'url': 'https://wiki.debian.org/SourcesList', 'notes': 'Canonical third-party source mechanism. Our enabled flag parallels APT source enable/disable; lastSynced ≈ apt-get update timestamp.'}]},
    'spec': {'name': 'spec', 'plural': 'specs', 'description': 'A spec — a design document describing work to be done.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'allDay', 'ty': 'boolean'}, {'name': 'currentUrl', 'ty': 'string'}, {'name': 'dateUpdated', 'ty': 'datetime'}, {'name': 'distinctId', 'ty': 'string'}, {'name': 'encoding', 'ty': 'string'}, {'name': 'endDate', 'ty': 'datetime'}, {'name': 'filename', 'ty': 'string'}, {'name': 'format', 'ty': 'string'}, {'name': 'icalUid', 'ty': 'string'}, {'name': 'kind', 'ty': 'string'}, {'name': 'labels', 'ty': 'stringlist'}, {'name': 'lineCount', 'ty': 'integer'}, {'name': 'mimeType', 'ty': 'string'}, {'name': 'parentId', 'ty': 'string'}, {'name': 'path', 'ty': 'string'}, {'name': 'priority', 'ty': 'integer'}, {'name': 'problem', 'ty': 'text'}, {'name': 'projectId', 'ty': 'string'}, {'name': 'properties', 'ty': 'json'}, {'name': 'recurrence', 'ty': 'stringlist'}, {'name': 'remoteId', 'ty': 'string'}, {'name': 'sha', 'ty': 'string'}, {'name': 'showAs', 'ty': 'string'}, {'name': 'size', 'ty': 'integer'}, {'name': 'sourceTitle', 'ty': 'string'}, {'name': 'sourceUrl', 'ty': 'url'}, {'name': 'startDate', 'ty': 'datetime'}, {'name': 'state', 'ty': 'string'}, {'name': 'status', 'ty': 'string'}, {'name': 'successCriteria', 'ty': 'text'}, {'name': 'target', 'ty': 'json'}, {'name': 'targetDate', 'ty': 'datetime'}, {'name': 'timezone', 'ty': 'string'}, {'name': 'visibility', 'ty': 'string'}], 'also': ['task', 'file'], 'display': {'subtitle': 'state', 'highlights': ['startDate', 'endDate', 'location']}, 'prior_art': [{'source': 'IETF RFC process', 'url': 'https://www.ietf.org/standards/rfcs/', 'notes': 'Canonical "design doc with problem statement and success criteria" lineage. Our problem/successCriteria mirror the RFC structure.'}, {'source': 'Architectural Decision Records (ADR / MADR)', 'url': 'https://adr.github.io/', 'notes': 'Modern in-repo equivalent. supersedes[] matches ADR\'s "Supersedes" link; dependsOn[] has no direct ADR peer.'}, {'source': 'Python PEP (spec-as-markdown)', 'url': 'https://peps.python.org/pep-0001/', 'notes': 'PEP states problem, rationale, spec, rejected alternatives. Our fields are a slim version of the PEP template.'}]},
    'subscription': {'name': 'subscription', 'plural': 'subscriptions', 'description': 'A standing subscription — a durable intent to stream live entities, re-armed on every engine boot.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'app', 'ty': 'string', 'required': True}, {'name': 'op', 'ty': 'string', 'required': True}, {'name': 'target', 'ty': 'string'}], 'identity': ['app', 'op'], 'display': {'subtitle': 'target'}, 'prior_art': [{'source': 'W3C WebSub subscriptions', 'url': 'https://www.w3.org/TR/websub/', 'notes': 'A subscription is a stored intent (topic + callback) the hub re-delivers against — content never lives on the subscription. Our app/op ≈ topic/callback.'}, {'source': 'MQTT persistent sessions', 'url': 'https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html', 'notes': 'Subscriptions survive connection loss and re-attach on reconnect. Our engine-boot re-arm parallels session resumption.'}, {'source': 'systemd unit enablement (systemctl enable)', 'url': 'https://www.freedesktop.org/software/systemd/man/systemctl.html', 'notes': 'Enablement is a durable on-disk fact distinct from the running process; boot re-creates the runtime state from it. Our node ≈ the wants/ symlink, the live CDP hook ≈ the running unit.'}]},
    'symbol': {'name': 'symbol', 'plural': 'symbols', 'description': 'A code symbol — one named thing in a source surface: an MCP tool/op, a', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'kind', 'ty': 'string'}, {'name': 'lang', 'ty': 'string'}, {'name': 'signature', 'ty': 'text'}, {'name': 'sourceLine', 'ty': 'integer'}, {'name': 'sourcePath', 'ty': 'string'}, {'name': 'summary', 'ty': 'text'}, {'name': 'urn', 'ty': 'string'}], 'display': {'subtitle': 'signature', 'body': 'summary', 'highlights': ['kind', 'lang', 'sourcePath']}, 'prior_art': [{'source': 'Language Server Protocol — DocumentSymbol / SymbolKind', 'url': 'https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_documentSymbol', 'notes': "SymbolKind (Function/Struct/Interface/Method/Module…) is the canonical `kind` enum; DocumentSymbol's name + detail + range → our name + signature + sourcePath/sourceLine."}, {'source': 'LSIF — Language Server Index Format', 'url': 'https://microsoft.github.io/language-server-protocol/specifications/lsif/0.6.0/specification/', 'notes': 'LSIF persists hover/definition/references as a graph of monikers across files — exactly our `urn` + calls/called_by trail, made queryable.'}, {'source': 'rustdoc JSON output format', 'url': 'https://doc.rust-lang.org/rustdoc/unstable-features.html#--output-format-json-output-crate-info-in-json', 'notes': "The P3 extractor's source — Item{id, name, kind, docs, links} maps item.id → urn, kind → kind, docs → body, inner.decl → signature."}, {'source': 'schema.org/SoftwareSourceCode + ctags', 'url': 'https://schema.org/SoftwareSourceCode', 'notes': "codeRepository/programmingLanguage → lang; ctags' (tag, file, kind) triple is the minimal symbol-index prior art for sourcePath + kind."}]},
    'tag': {'name': 'tag', 'plural': 'tags', 'description': 'A tag or label — Gmail label, Todoist label, GitHub label, git tag,', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'annotated', 'ty': 'boolean'}, {'name': 'color', 'ty': 'string'}, {'name': 'hash', 'ty': 'string'}, {'name': 'tagType', 'ty': 'string'}], 'identity': ['name'], 'display': {'title': 'name', 'subtitle': 'tagType'}, 'prior_art': [{'source': 'GitHub REST API — Labels', 'url': 'https://docs.github.com/en/rest/issues/labels', 'notes': "Our color/name/tagType ≈ GitHub Label's color/name/default."}, {'source': 'Gmail API — Labels', 'url': 'https://developers.google.com/gmail/api/reference/rest/v1/users.labels', 'notes': "Practical source. Our tagType distinguishes Gmail's SYSTEM vs USER label types."}, {'source': 'Dublin Core dc:subject', 'url': 'https://www.dublincore.org/specifications/dublin-core/dces/', 'notes': 'Generic classification vocabulary — tags on any resource.'}]},
    'task': {'name': 'task', 'plural': 'tasks', 'description': 'A work item — issue, ticket, or to-do. Supports hierarchy (parent/children)', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'allDay', 'ty': 'boolean'}, {'name': 'currentUrl', 'ty': 'string'}, {'name': 'dateUpdated', 'ty': 'datetime'}, {'name': 'distinctId', 'ty': 'string'}, {'name': 'endDate', 'ty': 'datetime'}, {'name': 'icalUid', 'ty': 'string'}, {'name': 'labels', 'ty': 'stringlist'}, {'name': 'parentId', 'ty': 'string'}, {'name': 'priority', 'ty': 'integer'}, {'name': 'projectId', 'ty': 'string'}, {'name': 'properties', 'ty': 'json'}, {'name': 'recurrence', 'ty': 'stringlist'}, {'name': 'remoteId', 'ty': 'string'}, {'name': 'showAs', 'ty': 'string'}, {'name': 'sourceTitle', 'ty': 'string'}, {'name': 'sourceUrl', 'ty': 'url'}, {'name': 'startDate', 'ty': 'datetime'}, {'name': 'state', 'ty': 'string'}, {'name': 'status', 'ty': 'string'}, {'name': 'target', 'ty': 'json'}, {'name': 'targetDate', 'ty': 'datetime'}, {'name': 'timezone', 'ty': 'string'}, {'name': 'visibility', 'ty': 'string'}], 'also': ['event'], 'identity': ['at', 'id'], 'display': {'subtitle': 'state', 'highlights': ['startDate', 'endDate', 'location']}, 'prior_art': [{'source': 'GitHub REST API — Issues', 'url': 'https://docs.github.com/en/rest/issues/issues', 'notes': 'Direct source. Our remoteId/state/labels/assignedTo/parent/ children/blockedBy/blocks map to GitHub Issue + sub-issues + task-list tracking.'}, {'source': 'Linear GraphQL API — Issue', 'url': 'https://developers.linear.app/docs/graphql/working-with-the-graphql-api', 'notes': "Practical canonical. Our priority/state/project/targetDate align with Linear's Issue model exactly."}, {'source': 'Todoist REST API v2 — Tasks', 'url': 'https://developer.todoist.com/rest/v2/', 'notes': 'Consumer-grade task model. Our startedAt/targetDate ≈ created_at/due; labels match directly.'}]},
    'tax_line': {'name': 'tax_line', 'plural': 'tax_lines', 'description': 'A single tax, fee, or surcharge line item on a priced commerce', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'amount', 'ty': 'number'}, {'name': 'appliesToIndex', 'ty': 'integer'}, {'name': 'code', 'ty': 'string'}, {'name': 'country', 'ty': 'string'}, {'name': 'currency', 'ty': 'string'}, {'name': 'description', 'ty': 'string'}, {'name': 'inclusive', 'ty': 'boolean'}, {'name': 'kind', 'ty': 'string'}, {'name': 'merchantImposed', 'ty': 'boolean'}, {'name': 'nature', 'ty': 'string'}, {'name': 'rate', 'ty': 'number'}, {'name': 'refundable', 'ty': 'boolean'}, {'name': 'taxableAmount', 'ty': 'number'}], 'identity': ['at', 'id'], 'display': {'subtitle': 'description'}, 'prior_art': [{'source': 'IATA List of Ticket and Airport Taxes and Fees (ILTATF)', 'url': 'https://www.iata.org/en/publications/store/list-of-ticket-and-airport-taxes-and-fees/', 'notes': "Canonical 1500+ entry registry of 2-char airline tax codes, grouped AT (airport), PC (passenger charge), ST (stamp), TT (ticket), MT (misc). Our `code` = ILTATF code when applicable; `nature` corresponds to ILTATF's grouping."}, {'source': 'IATA NDC Tax / TaxBreakdown element', 'url': 'https://developer.iata.org/en/ndc/', 'notes': "NDC's Price structure carries Taxes/Tax with TaxCode, CollectionPoint, CountryCode, Nature, Amount, Description. Our code/country/nature/amount/description map 1:1. NDC's Nature enum (security, fuel, facility, tax) informs our values."}, {'source': 'schema.org/UnitPriceSpecification + PriceComponentTypeEnumeration', 'url': 'https://schema.org/UnitPriceSpecification', 'notes': 'Generic commerce. priceComponentType ("Tax"), valueAddedTaxIncluded (our `inclusive`), priceCurrency. Lightweight; we add code, country, `imposedBy` to cover the authority-chain gap.'}, {'source': 'UBL 2.1 / Peppol BIS Billing 3.0 — TaxSubtotal / TaxCategory', 'url': 'https://docs.peppol.eu/poacc/billing/3.0/', 'notes': 'European eInvoicing. TaxSubtotal carries TaxableAmount, TaxAmount, Percent, TaxCategory/TaxScheme (VAT/GST). Our taxableAmount/amount/rate/nature align directly.'}, {'source': 'Stripe Invoice tax_amounts[]', 'url': 'https://docs.stripe.com/api/invoices/object', 'notes': "Stripe's line-item tax_amounts[] carries amount, inclusive, tax_rate, taxability_reason, taxable_amount. Our inclusive/ rate/taxableAmount match; jurisdiction/jurisdiction_level inspired the country + `imposedBy` split."}, {'source': 'Shopify Order tax_lines[]', 'url': 'https://shopify.dev/docs/api/admin-rest/latest/resources/order', 'notes': 'Minimal commerce model: price, rate, title, channel_liable. Our amount/rate/description map 1:1. Shopify allows multiple tax_lines per line item with same title + different rates — same pattern we need (US Transportation Tax recurring per segment). We disambiguate via appliesToIndex.'}, {'source': 'Avalara / TaxJar tax breakdown', 'url': 'https://developer.avalara.com/', 'notes': 'Commerce tax engines. Jurisdiction hierarchy (country / state / county / city / special) and combined tax rate. Informs the `imposedBy: actor` relation for layered jurisdictions (hotel occupancy + tourism + state sales tax, each their own line).'}]},
    'theme': {'name': 'theme', 'plural': 'themes', 'description': "An OS theme — a named knob-vector over its family's structure.", 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'defaultBackgroundColor', 'ty': 'string'}, {'name': 'description', 'ty': 'text'}, {'name': 'family', 'ty': 'string'}, {'name': 'startMenu', 'ty': 'string'}, {'name': 'style', 'ty': 'string'}, {'name': 'themeId', 'ty': 'string', 'required': True}], 'identity': ['themeId'], 'display': {'subtitle': 'family'}, 'prior_art': [{'source': 'System theme APIs (macOS NSAppearance, Windows WinUI)', 'url': 'https://developer.apple.com/documentation/appkit/nsappearance', 'notes': 'OS-level theme abstraction. Our `family` parallels NSAppearance.Name (aqua, darkAqua) and Windows theme families.'}]},
    'tool_call': {'name': 'tool_call', 'plural': 'tool_calls', 'description': 'A single tool invocation made by an agent during a message.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'durationMs', 'ty': 'integer'}, {'name': 'input', 'ty': 'text'}, {'name': 'isError', 'ty': 'boolean'}, {'name': 'output', 'ty': 'text'}], 'identity': ['platform', 'id'], 'display': {'subtitle': 'name'}, 'prior_art': [{'source': 'Anthropic Tool Use API', 'url': 'https://docs.anthropic.com/en/docs/build-with-claude/tool-use', 'notes': "Our name/input/output/isError map to tool_use/tool_result blocks in Claude's message API."}, {'source': 'OpenAI Function Calling / tool_calls', 'url': 'https://platform.openai.com/docs/guides/function-calling', 'notes': 'Our name/input = function.name/function.arguments; output is the tool-result message content.'}, {'source': 'OpenTelemetry GenAI semconv', 'url': 'https://opentelemetry.io/docs/specs/semconv/gen-ai/', 'notes': 'Emerging observability standard. Our durationMs/isError align with gen_ai.tool.* span attributes.'}]},
    'transaction': {'name': 'transaction', 'plural': 'transactions', 'description': 'A financial transaction — credit card charge, bank transfer, etc.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'allDay', 'ty': 'boolean'}, {'name': 'amount', 'ty': 'number'}, {'name': 'balance', 'ty': 'number'}, {'name': 'category', 'ty': 'string'}, {'name': 'currency', 'ty': 'string'}, {'name': 'currentUrl', 'ty': 'string'}, {'name': 'dateUpdated', 'ty': 'datetime'}, {'name': 'details', 'ty': 'json'}, {'name': 'distinctId', 'ty': 'string'}, {'name': 'endDate', 'ty': 'datetime'}, {'name': 'icalUid', 'ty': 'string'}, {'name': 'notes', 'ty': 'string'}, {'name': 'pending', 'ty': 'boolean'}, {'name': 'postingDate', 'ty': 'datetime'}, {'name': 'properties', 'ty': 'json'}, {'name': 'recurrence', 'ty': 'stringlist'}, {'name': 'recurring', 'ty': 'boolean'}, {'name': 'showAs', 'ty': 'string'}, {'name': 'sourceTitle', 'ty': 'string'}, {'name': 'sourceUrl', 'ty': 'url'}, {'name': 'startDate', 'ty': 'datetime'}, {'name': 'status', 'ty': 'string'}, {'name': 'timezone', 'ty': 'string'}, {'name': 'type', 'ty': 'string'}, {'name': 'visibility', 'ty': 'string'}], 'also': ['event'], 'identity': ['at', 'id'], 'display': {'subtitle': 'category', 'body': 'notes', 'highlights': ['amount', 'postingDate', 'currency']}, 'prior_art': [{'source': 'OFX (Open Financial Exchange) STMTTRN', 'url': 'https://financialdataexchange.org/ofx', 'notes': 'Direct source. Our amount/type/postingDate/balance map to STMTTRN TRNAMT/TRNTYPE/DTPOSTED/BALAMT.'}, {'source': 'ISO 20022 payments messaging', 'url': 'https://www.iso20022.org/', 'notes': 'Modern bank-messaging. Our currency = Ccy; category ≈ purpose code; details ≈ RemittanceInformation.'}, {'source': 'Plaid Transactions API', 'url': 'https://plaid.com/docs/api/products/transactions/', 'notes': "Practical mirror. Our category/pending/recurring/notes match Plaid's category/pending/personal_finance_category/name fields."}]},
    'transcript': {'name': 'transcript', 'plural': 'transcripts', 'description': 'A text transcript of audio/video content. Linked from meetings and videos.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'contentRole', 'ty': 'string'}, {'name': 'durationMs', 'ty': 'integer'}, {'name': 'language', 'ty': 'string'}, {'name': 'languageConfidence', 'ty': 'number'}, {'name': 'segmentCount', 'ty': 'integer'}, {'name': 'segments', 'ty': 'json'}, {'name': 'sourceType', 'ty': 'string'}], 'display': {'subtitle': 'language'}, 'prior_art': [{'source': 'WebVTT (W3C)', 'url': 'https://www.w3.org/TR/webvtt1/', 'notes': "Our segments are WebVTT cues (start/end/text). language follows WebVTT's LANGUAGE header."}, {'source': 'SRT SubRip Subtitles', 'url': 'https://matroska.org/technical/subtitles.html#srt-subtitles', 'notes': 'Practical alternative cue format. Same segment shape.'}, {'source': 'Whisper JSON output', 'url': 'https://github.com/openai/whisper', 'notes': 'Practical source — many transcript apps return Whisper-shaped JSON (segments with start/end/text). Direct match.'}]},
    'transition': {'name': 'transition', 'plural': 'transitions', 'description': 'An identity change — name, gender, religion, sports team, anything', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'additionalName', 'ty': 'string'}, {'name': 'allDay', 'ty': 'boolean'}, {'name': 'currentUrl', 'ty': 'string'}, {'name': 'dateUpdated', 'ty': 'datetime'}, {'name': 'distinctId', 'ty': 'string'}, {'name': 'endDate', 'ty': 'datetime'}, {'name': 'familyName', 'ty': 'string'}, {'name': 'gender', 'ty': 'string'}, {'name': 'givenName', 'ty': 'string'}, {'name': 'honorificPrefix', 'ty': 'string'}, {'name': 'honorificSuffix', 'ty': 'string'}, {'name': 'icalUid', 'ty': 'string'}, {'name': 'legalName', 'ty': 'string'}, {'name': 'maidenName', 'ty': 'string'}, {'name': 'nameOrder', 'ty': 'string'}, {'name': 'nickname', 'ty': 'string'}, {'name': 'phoneticFamilyName', 'ty': 'string'}, {'name': 'phoneticGivenName', 'ty': 'string'}, {'name': 'properties', 'ty': 'json'}, {'name': 'recurrence', 'ty': 'stringlist'}, {'name': 'showAs', 'ty': 'string'}, {'name': 'sortAs', 'ty': 'string'}, {'name': 'sourceTitle', 'ty': 'string'}, {'name': 'sourceUrl', 'ty': 'url'}, {'name': 'startDate', 'ty': 'datetime'}, {'name': 'status', 'ty': 'string'}, {'name': 'timezone', 'ty': 'string'}, {'name': 'visibility', 'ty': 'string'}], 'also': ['event'], 'display': {'subtitle': 'startDate', 'highlights': ['startDate', 'givenName', 'familyName', 'gender']}, 'prior_art': [{'source': 'Event Sourcing (Fowler)', 'url': 'https://martinfowler.com/eaaDev/EventSourcing.html', 'notes': 'Past-tense events as facts; entity state = fold over the event stream. `transition` is the past-tense event-node; the `latest:` resolver is the fold. Reuses canonical field names — no `new_*` prefix per the event-sourcing convention.'}, {'source': 'Palantir Foundry — Action Log Objects', 'url': 'https://www.palantir.com/docs/foundry/announcements/2022-10/index.html', 'notes': 'Palantir reifies every mutation as a queryable Action Log Object — same shape as our reified `transition` event. They type Actions per-mutation (`AssignEmployee` etc.); we collapse to one umbrella shape with optional fields for agent-OS ergonomics (operations not known in advance).'}, {'source': 'IMO / GISIS maritime registry — particulars change', 'url': 'https://gisis.imo.org/public/default.aspx', 'notes': '50-year-old domain proves the pattern: stable identifier (IMO number) + canonical property names + reified change events (name/flag/owner change). `Person.id` ↔ `Ship.imo`; `transition.gender` ↔ a `flag_change` on a ship.'}, {'source': 'FHIR R5 HumanName.use + HumanName.period', 'url': 'https://hl7.org/fhir/datatypes.html#HumanName', 'notes': 'FHIR encodes dated names via multi-value on the Patient (no event-node). We lift the same pattern to an event-node because the change has its own date + place + authority context worth capturing as a first-class graph entity.'}, {'source': 'Wikidata P735/P734/P21 + P580/P582 qualifiers', 'url': 'https://www.wikidata.org/wiki/Property:P735', 'notes': 'Property statements with start-time/end-time qualifiers. Validates "reuse canonical field name + date positions in time".'}]},
    'trip': {'name': 'trip', 'plural': 'trips', 'description': 'A directed journey from origin to destination — one direction of travel.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'allDay', 'ty': 'boolean'}, {'name': 'arrivalTime', 'ty': 'datetime'}, {'name': 'bookingToken', 'ty': 'string'}, {'name': 'cabinClass', 'ty': 'string'}, {'name': 'carbonEmissions', 'ty': 'json'}, {'name': 'currency', 'ty': 'string'}, {'name': 'currentUrl', 'ty': 'string'}, {'name': 'dateUpdated', 'ty': 'datetime'}, {'name': 'departureTime', 'ty': 'datetime'}, {'name': 'distance', 'ty': 'string'}, {'name': 'distinctId', 'ty': 'string'}, {'name': 'duration', 'ty': 'string'}, {'name': 'durationMinutes', 'ty': 'integer'}, {'name': 'endDate', 'ty': 'datetime'}, {'name': 'fare', 'ty': 'string'}, {'name': 'fareAmount', 'ty': 'number'}, {'name': 'guest', 'ty': 'json'}, {'name': 'icalUid', 'ty': 'string'}, {'name': 'isPool', 'ty': 'boolean'}, {'name': 'isReserve', 'ty': 'boolean'}, {'name': 'isScheduled', 'ty': 'boolean'}, {'name': 'isSurge', 'ty': 'boolean'}, {'name': 'marketplace', 'ty': 'string'}, {'name': 'properties', 'ty': 'json'}, {'name': 'rating', 'ty': 'string'}, {'name': 'recurrence', 'ty': 'stringlist'}, {'name': 'showAs', 'ty': 'string'}, {'name': 'sourceTitle', 'ty': 'string'}, {'name': 'sourceUrl', 'ty': 'url'}, {'name': 'startDate', 'ty': 'datetime'}, {'name': 'status', 'ty': 'string'}, {'name': 'stops', 'ty': 'integer'}, {'name': 'timezone', 'ty': 'string'}, {'name': 'trackingUrl', 'ty': 'url'}, {'name': 'tripType', 'ty': 'string'}, {'name': 'vehicle', 'ty': 'json'}, {'name': 'vehicleType', 'ty': 'string'}, {'name': 'visibility', 'ty': 'string'}], 'also': ['event'], 'identity': ['at', 'id'], 'display': {'subtitle': 'tripType', 'highlights': ['startDate', 'endDate', 'location']}, 'prior_art': [{'source': 'schema.org/Trip + subTrip', 'url': 'https://schema.org/Trip', 'notes': 'Our origin/destination/departureTime/arrivalTime map exactly; legs[] ≈ subTrip or itinerary.'}, {'source': 'IATA NDC Slice (airline itineraries)', 'url': 'https://www.iata.org/en/programs/airline-distribution/retailing/ndc/', 'notes': 'NDC slice = our trip; NDC segment = our leg. cabinClass, bookingToken come from NDC offer items.'}, {'source': 'Uber API — Trip resource', 'url': 'https://developer.uber.com/docs/riders/references/api', 'notes': "Practical source for ride trips. Our fare/fareAmount/ trackingUrl/isSurge/isScheduled lifted from Uber's Trip model."}]},
    'unit': {'name': 'unit', 'plural': 'units', 'description': 'A unit of measure — a concrete scale for a quantity. mg/dL, USD, pascal,', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'iso4217', 'ty': 'string'}, {'name': 'iso4217Numeric', 'ty': 'string'}, {'name': 'kind', 'ty': 'string'}, {'name': 'label', 'ty': 'string'}, {'name': 'logBase', 'ty': 'number'}, {'name': 'minorExponent', 'ty': 'integer'}, {'name': 'qudtUnitIri', 'ty': 'string'}, {'name': 'siDigitalFrameworkUri', 'ty': 'string'}, {'name': 'symbol', 'ty': 'string'}, {'name': 'toBaseFactor', 'ty': 'number'}, {'name': 'toBaseOffset', 'ty': 'number'}, {'name': 'ucumCode', 'ty': 'string'}, {'name': 'unCefactCommonCode', 'ty': 'string'}, {'name': 'wikidataId', 'ty': 'string'}], 'identity_any': ['ucumCode', 'siDigitalFrameworkUri', 'iso4217'], 'display': {'subtitle': 'symbol'}, 'prior_art': [{'source': 'UCUM — Unified Code for Units of Measure', 'url': 'https://ucum.org/ucum', 'notes': 'ucumCode is the primary working identity — case-sensitive variant (mg is not MG; h hour is not H henry). Compositional, and the de-facto healthcare standard (FHIR Quantity mandates it, LOINC and HL7 use it). Machine-readable database: ucum-essence.xml.'}, {'source': 'BIPM — SI Digital Framework / SI Reference Point', 'url': 'https://www.si-digital-framework.org/', 'notes': 'Launched March 2024 by the BIPM CIPM Task Group on the Digital SI. Publishes resolvable persistent URIs for SI units, prefixes, and defining constants (base namespace si-digital-framework.org/SI/ units/), served as TTL plus a JSON/XML API. The most authoritative source for SI units — treaty-level. siDigitalFrameworkUri carries it; null for non-SI units, and that null is meaningful.'}, {'source': 'UN/CEFACT Recommendation 20 — Codes for Units of Measure Used in International Trade', 'url': 'https://unece.org/trade/uncefact/cl-recommendations', 'notes': "Around 700 short codes (KGM kilogram, MTR metre, LTR litre, CEL degree Celsius). Rev 17 (2021), freely downloadable as XLSX or genericode XML. schema.org's unitCode property uses exactly these codes — unCefactCommonCode is the interop join key."}, {'source': 'QUDT — Quantities, Units, Dimensions and Types', 'url': 'https://www.qudt.org/doc/DOC_VOCAB-UNITS.html', 'notes': 'qudtUnitIri cross-references QUDT, itself a cross-reference hub (QUDT units carry qudt:ucumCode, qudt:uneceCommonCode, qudt:wikidataMatch). toBaseFactor/toBaseOffset correspond to qudt:conversionMultiplier / conversionOffset; kind=currency corresponds to qudt:CurrencyUnit, which also carries NO conversion multiplier — FX is external.'}, {'source': 'Wikidata', 'url': 'https://www.wikidata.org/wiki/Q11570', 'notes': 'wikidataId (kilogram = Q11570) is a universal glue identifier — links to every Wikipedia language edition and many external databases. Free SPARQL endpoint plus dumps.'}, {'source': 'ISO 4217 — Currency codes', 'url': 'https://www.iso.org/iso-4217-currency-codes.html', 'notes': 'iso4217 (alpha) plus iso4217Numeric and minorExponent for currency units. ISO 4217 IS the authoritative currency-code registry — notably, currency is the ONE unit family with a single authoritative code system; physical units have none.'}, {'source': 'schema.org — unitCode', 'url': 'https://schema.org/unitCode', 'notes': 'Precedent that the minimum unit model is (value, unitCode), and that unitCode in practice means a UN/CEFACT Rec 20 code.'}, {'source': 'NIST SP 811 / SP 330 — and why NIST is NOT a field', 'url': 'https://www.nist.gov/pml/special-publication-811', 'notes': 'Recorded deliberately. NIST publishes SI usage guidance (SP 811) and the US edition of the SI Brochure (SP 330) — prose only. NIST assigns no unit codes and maintains no unit registry; there is nothing to cross-reference, so no NIST field exists on this shape. Same for ISO 80000 — it defines units in prose and assigns no codes.'}]},
    'user': {'name': 'user', 'plural': 'users', 'description': 'An AgentOS user — the **seat** at this machine. Pure OS bookkeeping:', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'actorType', 'ty': 'string'}, {'name': 'osUsername', 'ty': 'string'}, {'name': 'primaryUser', 'ty': 'boolean'}], 'also': ['actor'], 'identity_any': ['osUsername'], 'display': {'subtitle': 'name'}, 'prior_art': [{'source': 'POSIX getpwuid (passwd database)', 'url': 'https://pubs.opengroup.org/onlinepubs/9699919799/functions/getpwuid.html', 'notes': 'The OS-level "user" — uid + login name + home dir. Our `osUsername` mirrors `pw_name`; identity-by-OS-account follows the same pattern. We diverge by separating the OS seat (`user`) from the human (`person`); POSIX conflates them.'}, {'source': 'schema.org/Audience', 'url': 'https://schema.org/Audience', 'notes': 'Loose fit. schema.org has no "OS user" concept — user accounts are product-specific. We model it explicitly because AgentOS is the product, and the seat is the machine\'s record of the human.'}]},
    'user_identity': {'name': 'user_identity', 'plural': 'user_identities', 'description': 'An identity claim — "the engine-level user X identifies as person:Y', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'active', 'ty': 'boolean'}, {'name': 'person_node_id', 'ty': 'string'}, {'name': 'user_id', 'ty': 'string'}, {'name': 'volume_id', 'ty': 'string'}], 'display': {'subtitle': 'volume_id', 'highlights': ['person_node_id', 'active']}, 'prior_art': [{'source': 'Solid (Tim Berners-Lee)', 'url': 'https://solidproject.org/faq', 'notes': 'Solid Pod ↔ WebID is the per-user identity model. A Solid user owns one personal pod whose WebID is the authoritative identity; cross-pod identity is a single relation. We split: User is engine state; Person is graph content; user_identity is the explicit bridge that can be many-to-many across volumes.'}, {'source': 'Unix/macOS — /etc/passwd vs /Users/<u>', 'url': 'https://en.wikipedia.org/wiki/Passwd', 'notes': 'OS users (engine.db::users) and home directories (~/.agentos/users/<u>.db) follow the Unix convention. The identity *within* the home is content the home owns.'}]},
    'video': {'name': 'video', 'plural': 'videos', 'description': 'A video file — the media artifact, not the social context around it.', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'codec', 'ty': 'string'}, {'name': 'copyrightYear', 'ty': 'integer'}, {'name': 'coverage', 'ty': 'string'}, {'name': 'dateCreated', 'ty': 'date'}, {'name': 'description', 'ty': 'string'}, {'name': 'durationMs', 'ty': 'integer'}, {'name': 'encoding', 'ty': 'string'}, {'name': 'filename', 'ty': 'string'}, {'name': 'format', 'ty': 'string'}, {'name': 'frameRate', 'ty': 'number'}, {'name': 'kind', 'ty': 'string'}, {'name': 'language', 'ty': 'string'}, {'name': 'license', 'ty': 'string'}, {'name': 'lineCount', 'ty': 'integer'}, {'name': 'mimeType', 'ty': 'string'}, {'name': 'path', 'ty': 'string'}, {'name': 'resolution', 'ty': 'string'}, {'name': 'sha', 'ty': 'string'}, {'name': 'size', 'ty': 'integer'}, {'name': 'tags', 'ty': 'stringlist'}, {'name': 'viewCount', 'ty': 'integer'}], 'also': ['creative_work', 'file'], 'identity_any': ['sha', 'url'], 'display': {'subtitle': 'author', 'image': 'image', 'body': 'description', 'highlights': ['datePublished', 'published_by']}, 'prior_art': [{'source': 'schema.org/VideoObject', 'url': 'https://schema.org/VideoObject', 'notes': 'Our durationMs ≈ duration (ISO 8601 period); resolution ≈ videoFrameSize; frameRate has no direct property; codec ≈ encodingFormat.'}, {'source': 'IANA Media Types (video/*)', 'url': 'https://www.iana.org/assignments/media-types/media-types.xhtml#video', 'notes': 'Our codec values map to registered video/* media types (mp4, webm, ogg).'}, {'source': 'MPEG / ITU video codec specs', 'url': 'https://www.itu.int/rec/T-REC-H.264', 'notes': 'Canonical codec definitions. Our codec values are MPEG/ITU codec short names (h264, vp9, av1).'}]},
    'volume': {'name': 'volume', 'plural': 'volumes', 'description': 'A mounted Volume — any named source of typed nodes the engine has', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'address', 'ty': 'string'}, {'name': 'auto_mount', 'ty': 'boolean'}, {'name': 'default_view', 'ty': 'string'}, {'name': 'ejectable', 'ty': 'boolean'}, {'name': 'freeBytes', 'ty': 'integer'}, {'name': 'icon', 'ty': 'string'}, {'name': 'kind', 'ty': 'string'}, {'name': 'provider', 'ty': 'string'}, {'name': 'readOnly', 'ty': 'boolean'}, {'name': 'removable', 'ty': 'boolean'}, {'name': 'scope', 'ty': 'string'}, {'name': 'source', 'ty': 'string'}, {'name': 'totalBytes', 'ty': 'integer'}, {'name': 'volume_id', 'ty': 'string'}], 'display': {'subtitle': 'kind'}, 'prior_art': [{'source': 'HDT (Header, Dictionary, Triples)', 'url': 'https://www.rdfhdt.org/what-is-hdt/', 'notes': 'RDF binary file format; one file = one queryable graph. The Header describes the dataset in its own vocabulary — same shapes-ride-along move as our embedded ontology.'}, {'source': 'Stardog Virtual Graphs', 'url': 'https://docs.stardog.com/virtual-graphs/', 'notes': 'Register an external source under a URI; query as a named graph. Our volume shape is the registration row; mount/unmount is the verb pair.'}, {'source': 'macOS Disk Utility / DMG', 'url': 'https://support.apple.com/guide/disk-utility/welcome/mac', 'notes': 'The UX mental model. A volume is an attached, browseable disk; the Finder shows it in the sidebar; eject detaches it without destroying the underlying file.'}]},
    'vote': {'name': 'vote', 'plural': 'votes', 'description': 'A dated, directional endorsement of an issue. Each cast is its OWN node,', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string'}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'direction', 'ty': 'string'}, {'name': 'instance', 'ty': 'string'}, {'name': 'note', 'ty': 'text'}], 'display': {'subtitle': 'direction', 'body': 'note'}, 'prior_art': [{'source': 'Canny / Featurebase vote object', 'url': 'https://developers.canny.io/api-reference', 'notes': "A vote is an object (voter + post + created date), not a counter — so duplicates merge and votes roll up. Our `for`/`cast_by`/`date` mirror Canny's post/voter/created; score is derived from the set, never stored."}, {'source': 'ActivityStreams 2.0 Like', 'url': 'https://www.w3.org/TR/activitystreams-vocabulary/#dfn-like', 'notes': 'A Like is an Activity with actor + object — our cast_by ≈ actor, for ≈ object. We add `direction` (up/down) and `note`/`instance` for evidence-bearing agent recurrence, which AS2 Like lacks.'}]},
    'webpage': {'name': 'webpage', 'plural': 'webpages', 'description': 'A web page. Base type for search result. Also used for browser history', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string', 'required': True}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'contentType', 'ty': 'string'}, {'name': 'error', 'ty': 'string'}, {'name': 'favicon', 'ty': 'url'}, {'name': 'lastVisitUnix', 'ty': 'integer'}, {'name': 'visitCount', 'ty': 'integer'}], 'identity': ['url'], 'display': {'subtitle': 'url'}, 'prior_art': [{'source': 'schema.org/WebPage', 'url': 'https://schema.org/WebPage', 'notes': "Our URL-as-identity matches schema.org's @id/url convention; contentType ≈ encodingFormat."}, {'source': 'HTTP semantics (RFC 9110)', 'url': 'https://datatracker.ietf.org/doc/html/rfc9110', 'notes': 'Our contentType is the Content-Type response header; error ≈ non-2xx status text.'}, {'source': 'Chrome history / WebExtensions History API', 'url': 'https://developer.chrome.com/docs/extensions/reference/api/history', 'notes': "Practical source. Our visitCount/lastVisitUnix lift from the history API's VisitItem structure."}]},
    'website': {'name': 'website', 'plural': 'websites', 'description': 'A published website (not a single page — see webpage for that).', 'fields': [{'name': 'name', 'ty': 'string', 'required': True}, {'name': 'text', 'ty': 'string'}, {'name': 'url', 'ty': 'string', 'required': True}, {'name': 'image', 'ty': 'string'}, {'name': 'author', 'ty': 'string'}, {'name': 'datePublished', 'ty': 'string'}, {'name': 'content', 'ty': 'string'}, {'name': 'anonymous', 'ty': 'boolean'}, {'name': 'claimToken', 'ty': 'string'}, {'name': 'claimUrl', 'ty': 'url'}, {'name': 'status', 'ty': 'string'}, {'name': 'versionId', 'ty': 'string'}], 'identity': ['url'], 'display': {'subtitle': 'url'}, 'prior_art': [{'source': 'schema.org/WebSite', 'url': 'https://schema.org/WebSite', 'notes': 'Our url-as-identity matches; ownedBy ≈ publisher; domain relation ≈ url host.'}, {'source': 'WHOIS (RFC 3912)', 'url': 'https://datatracker.ietf.org/doc/html/rfc3912', 'notes': 'Our expiresAt/domain source from WHOIS records; claimToken has no direct WHOIS peer (HERE.NOW-specific).'}, {'source': 'RFC 7033 WebFinger (host-meta)', 'url': 'https://datatracker.ietf.org/doc/html/rfc7033', 'notes': 'Website metadata discovery. Our claimUrl parallels /.well-known/host-meta patterns.'}]},
}

# Identity keys per shape — sidecars for the app worker.
SHAPE_IDENTITIES: dict[str, list[str]] = {
    'account': ['at', 'identifier'],
    'aircraft': ['icaoCode'],
    'airline': ['iataCode'],
    'airport': ['iataCode'],
    'app': ['id'],
    'booking_offer': ['at', 'cartId'],
    'bookmark': ['points_to'],
    'brand': ['url'],
    'calendar': ['at', 'calendarId'],
    'channel': ['at', 'id'],
    'community': ['at', 'id'],
    'conversation': ['at', 'id'],
    'credential': ['domain', 'identifier', 'itemType'],
    'dimension': ['key'],
    'dns_record': ['domain', 'recordType', 'recordName'],
    'domain': ['name'],
    'email': ['at', 'id'],
    'event': ['at', 'id'],
    'fare': ['at', 'identifier'],
    'financial_account': ['at', 'identifier'],
    'group': ['at', 'id'],
    'health-reference-range': ['analyte', 'issuingLab', 'method', 'startDate'],
    'insurance_policy': ['underwritten_by', 'policyNumber'],
    'invitation': ['at', 'id'],
    'list': ['at', 'id'],
    'mcp_session': ['client', 'projectId', 'gitBranch'],
    'membership': ['at', 'id'],
    'message': ['at', 'id'],
    'model': ['at', 'name'],
    'offer': ['id'],
    'order': ['at', 'orderId'],
    'organization': ['name'],
    'pass': ['at', 'id'],
    'payment_method': ['at', 'identifier'],
    'podcast': ['at', 'id'],
    'post': ['at', 'id'],
    'project': ['at', 'id'],
    'protocol': ['name'],
    'quantity-kind': ['key'],
    'reservation': ['at', 'reservationId'],
    'seatmap': ['id'],
    'service': ['id'],
    'shape': ['name'],
    'source': ['address'],
    'subscription': ['app', 'op'],
    'tag': ['name'],
    'task': ['at', 'id'],
    'tax_line': ['at', 'id'],
    'theme': ['themeId'],
    'tool_call': ['platform', 'id'],
    'transaction': ['at', 'id'],
    'trip': ['at', 'id'],
    'webpage': ['url'],
    'website': ['url'],
}

SHAPE_IDENTITIES_ANY: dict[str, list[str]] = {
    'book': ['isbn13', 'isbn'],
    'cursor': ['sha', 'url'],
    'file': ['sha', 'url'],
    'font': ['family', 'postscriptName'],
    'health-biomarker': ['loincCode', 'measure'],
    'health-condition': ['snomedCode', 'name'],
    'health-lab': ['cliaNumber', 'url'],
    'health-procedure': ['cptCode', 'snomedCode', 'id'],
    'icon': ['component', 'url'],
    'image': ['sha', 'url'],
    'intellectual_property': ['identifier'],
    'person': ['url'],
    'place': ['googlePlaceId', 'mapboxId'],
    'product': ['url'],
    'qualification': ['identifier'],
    'repository': ['path', 'url'],
    'software': ['url'],
    'sound': ['sha', 'url'],
    'unit': ['ucumCode', 'siDigitalFrameworkUri', 'iso4217'],
    'user': ['osUsername'],
    'video': ['sha', 'url'],
}

# YAML declaration order per shape — author order is meaning.
SHAPE_FIELD_ORDER: dict[str, list[str]] = {
    'account': ['identifier', 'handle', 'displayName', 'display', 'email', 'phone', 'bio', 'accountType', 'color', 'isActive', 'joinedDate', 'lastActive', 'lastProfileFetch', 'userId', 'issuer', 'metadata'],
    'activity': ['action', 'changedKeys', 'toolName', 'duration', 'success', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'status', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'actor': ['actorType'],
    'aircraft': ['model', 'variant', 'seatCapacity', 'rangeKm', 'iataCode', 'icaoCode', 'category', 'price', 'priceAmount', 'originalPrice', 'originalPriceAmount', 'currency', 'categories', 'availability', 'images', 'quantity', 'weight', 'weightValue', 'weightUnit', 'soldByWeight', 'department', 'aisle', 'sku', 'barcode', 'nutritionScore', 'novaGroup', 'calories', 'servingSize', 'customizationGroups'],
    'airline': ['iataCode', 'icaoCode', 'callsign', 'country', 'alliance', 'industry', 'actorType'],
    'airport': ['iataCode', 'icaoCode', 'city', 'country', 'countryCode', 'timezone', 'elevationFt', 'terminalCount'],
    'app': ['id', 'name', 'description', 'color', 'status', 'error', 'iconRole', 'route', 'defaultRoute', 'defaultView', 'isSystem', 'handles', 'composition', 'account'],
    'auth_challenge': ['kind', 'payload', 'artifact', 'instructions', 'retrieval', 'expiresAt', 'continueWith'],
    'birth': ['givenName', 'additionalName', 'familyName', 'honorificPrefix', 'honorificSuffix', 'legalName', 'maidenName', 'sortAs', 'nameOrder', 'phoneticGivenName', 'phoneticFamilyName', 'gender', 'nickname', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'status', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'book': ['isbn', 'isbn13', 'pages', 'genres', 'series', 'format', 'language', 'originalTitle', 'places', 'characters', 'awardsWon', 'name', 'description', 'license', 'copyrightYear', 'datePublished', 'dateCreated', 'url', 'coverage', 'tags', 'category', 'price', 'priceAmount', 'originalPrice', 'originalPriceAmount', 'currency', 'categories', 'availability', 'images', 'quantity', 'weight', 'weightValue', 'weightUnit', 'soldByWeight', 'department', 'aisle', 'sku', 'barcode', 'nutritionScore', 'novaGroup', 'calories', 'servingSize', 'customizationGroups'],
    'booking_offer': ['cartId', 'referenceNumber', 'status', 'preparedAt', 'presentedAt', 'approvedAt', 'expiresAt', 'currency', 'baseAmount', 'taxAmount', 'feesAmount', 'totalAmount', 'itineraryHash', 'signature', 'signatureAlg', 'signedBy', 'checkoutUrl', 'confirmEndpoint', 'isRefundable', 'isChangeable', 'hasVoidWindow', 'voidWindowEndsAt', 'conditions', 'blob', 'review', 'contactEmail', 'contactPhone', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'bookmark': ['name', 'handle', 'address'],
    'branch': ['commit', 'upstream', 'ahead', 'behind', 'isCurrent', 'isRemote'],
    'brand': ['tagline', 'country', 'primaryColor', 'textColor'],
    'calendar': ['calendarId', 'color', 'backgroundColor', 'foregroundColor', 'isPrimary', 'isReadonly', 'accessRole', 'source', 'timezone'],
    'channel': ['banner', 'subscriberCount'],
    'class': ['activityType', 'capacity', 'spotsRemaining', 'isFull', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'status', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'community': ['privacy', 'memberCount', 'subscriberCount', 'allowCrypto'],
    'conversation': ['isGroup', 'isArchived', 'unreadCount', 'messageCount', 'accountEmail', 'historyId', 'source', 'cwd', 'gitBranch'],
    'conversion': ['kind', 'factor', 'rate', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'status', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'creative_work': ['name', 'description', 'license', 'copyrightYear', 'datePublished', 'dateCreated', 'url', 'language', 'coverage', 'tags'],
    'credential': ['domain', 'identifier', 'itemType', 'source', 'obtainedAt', 'lastVerified', 'refreshable', 'storeRowId'],
    'cursor': ['hotspotX', 'hotspotY', 'dimension', 'format', 'purpose', 'name', 'description', 'license', 'copyrightYear', 'datePublished', 'dateCreated', 'url', 'language', 'coverage', 'tags', 'filename', 'mimeType', 'size', 'path', 'encoding', 'lineCount', 'kind', 'sha'],
    'dimension': ['key', 'label', 'length', 'mass', 'time', 'current', 'temperature', 'amount', 'luminous', 'dimensionless'],
    'dns_record': ['domain', 'recordName', 'recordType', 'type', 'ttl', 'priority', 'recordId', 'values'],
    'document': ['contentType', 'language', 'wordCount', 'abstract', 'tableOfContents', 'filename', 'mimeType', 'size', 'path', 'format', 'encoding', 'lineCount', 'kind', 'sha'],
    'domain': ['status', 'registrar', 'autoRenew', 'nameservers'],
    'email': ['subject', 'messageId', 'inReplyTo', 'isUnread', 'isStarred', 'isDraft', 'isSent', 'isTrash', 'isSpam', 'hasAttachments', 'draftId', 'conversationId', 'accountEmail', 'sizeEstimate', 'references', 'replyTo', 'deliveredTo', 'attachments', 'toRaw', 'ccRaw', 'bccRaw', 'unsubscribe', 'unsubscribeOneClick', 'manageSubscription', 'listId', 'isAutomated', 'precedence', 'mailer', 'returnPath', 'authResults', 'isOutgoing'],
    'episode': ['durationMs', 'episodeNumber', 'seasonNumber'],
    'event': ['startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'status', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'fare': ['identifier', 'bookingCode', 'productType', 'fareFamily', 'class', 'basePrice', 'currency', 'passengerType', 'milesEarned', 'pointsEarned', 'components', 'refundable', 'changeable', 'restrictions', 'conditions'],
    'file': ['filename', 'mimeType', 'size', 'path', 'format', 'encoding', 'lineCount', 'kind', 'sha'],
    'financial_account': ['identifier', 'accountId', 'accountNumber', 'routingNumber', 'last4', 'currency', 'accountType', 'balance', 'available', 'creditLimit', 'minimumPayment', 'cardType', 'interestRate'],
    'flight': ['flightNumber', 'durationMinutes', 'cabinClass', 'stops', 'carbonEmissions', 'sequence', 'departureTime', 'arrivalTime', 'duration', 'vehicleType', 'layoverMinutes', 'trace', 'tracePointCount', 'polyline', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'status', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'font': ['family', 'genericFamily', 'postscriptName', 'weights', 'styles', 'formats', 'scripts', 'glyphCount', 'designerUrl', 'vendorUrl', 'licenseInfoUrl', 'name', 'description', 'license', 'copyrightYear', 'datePublished', 'dateCreated', 'url', 'language', 'coverage', 'tags'],
    'git_commit': ['sha', 'shortHash', 'message', 'additions', 'deletions', 'filesChanged', 'committedAt', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'status', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'group': ['memberCount', 'category'],
    'health-biomarker': ['measure', 'category', 'loincCode', 'analyteType', 'description'],
    'health-condition': ['clinicalStatus', 'verificationStatus', 'proximity', 'bodySite', 'severity', 'snomedCode', 'icd10Code', 'clinicalArea', 'mitigation', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'status', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'health-immunization': ['dateAdministered', 'cvxCode', 'manufacturer', 'lotNumber', 'doseNumber', 'seriesDoses', 'site', 'route', 'diseaseTarget', 'notes', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'status', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'health-lab': ['cliaNumber', 'npi', 'ccn', 'labType', 'accreditation', 'industry', 'actorType'],
    'health-panel': ['panelCode', 'fasting', 'description', 'id', 'listId', 'listType', 'ordering_mode', 'member_shape', 'privacy', 'isDefault', 'isPublic', 'itemCount', 'arrangement', 'default_view', 'icon_size', 'sort_by', 'path', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'status', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'health-procedure': ['performedDate', 'procedureType', 'bodySite', 'outcome', 'status', 'cptCode', 'snomedCode', 'findings', 'followUp', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'health-reference-range': ['low', 'high', 'unit', 'refText', 'category', 'provenance', 'method', 'ageLow', 'ageHigh', 'sex', 'pregnancy', 'gestationalAge', 'fasting', 'timeOfDay', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'status', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'icon': ['dimension', 'format', 'url', 'component', 'purpose', 'style', 'name', 'description', 'license', 'copyrightYear', 'datePublished', 'dateCreated', 'language', 'coverage', 'tags'],
    'image': ['width', 'height', 'format', 'altText', 'appName', 'windowId', 'displayId', 'displayIndex', 'name', 'description', 'license', 'copyrightYear', 'datePublished', 'dateCreated', 'url', 'language', 'coverage', 'tags', 'filename', 'mimeType', 'size', 'path', 'encoding', 'lineCount', 'kind', 'sha'],
    'insurance_coverage': ['limit', 'limitBasis', 'deductible', 'outOfPocketMax', 'copay', 'coinsurance', 'currency', 'requiresPreauth', 'requiresReferral', 'waitingPeriodMonths', 'notes'],
    'insurance_policy': ['coverageType', 'policyNumber', 'memberId', 'groupNumber', 'network', 'status', 'tier', 'autoRenew', 'price', 'currency', 'billingType', 'useCount', 'guestPassQuantity', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'intellectual_property': ['category', 'mark', 'identifier', 'register', 'status', 'filingBasis', 'niceClass', 'validIn', 'renewalPeriod', 'verificationUrl'],
    'invitation': ['invitationType', 'email', 'role', 'status', 'token', 'acceptedAt', 'revokedAt', 'message', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'issue': ['declined', 'externalUrl', 'postType', 'score', 'commentCount', 'community'],
    'launch': ['flightNumber', 'rocketId', 'launchpadId', 'crewIds', 'reusedBoosters', 'landingOutcomes', 'articleUrl', 'webcastUrl', 'wikipediaUrl', 'patchImage', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'status', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'leg': ['sequence', 'departureTime', 'arrivalTime', 'duration', 'durationMinutes', 'flightNumber', 'cabinClass', 'vehicleType', 'layoverMinutes', 'carbonEmissions', 'trace', 'tracePointCount', 'polyline', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'status', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'list': ['id', 'listId', 'listType', 'ordering_mode', 'member_shape', 'privacy', 'isDefault', 'isPublic', 'itemCount', 'arrangement', 'default_view', 'icon_size', 'sort_by', 'path'],
    'loaded_model': ['size', 'quantization', 'vramUsage', 'sizeVram', 'digest', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'status', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'mcp_session': ['client', 'projectId', 'gitBranch', 'sessionType', 'startedAt', 'endedAt', 'messageCount', 'tokenCount'],
    'measure': ['value', 'valueText', 'refLow', 'refHigh', 'refText', 'flag', 'status', 'notes', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'meeting': ['calendarLink', 'isVirtual', 'meetingUrl', 'conferenceProvider', 'phoneDialIn', 'meetingType', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'status', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'membership': ['status', 'tier', 'autoRenew', 'price', 'currency', 'billingType', 'useCount', 'guestPassQuantity', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'message': ['isOutgoing', 'isStarred', 'conversationId'],
    'model': ['contextLength', 'contextWindow', 'maxOutput', 'pricingInput', 'pricingOutput', 'modality', 'modelType', 'quantization', 'quantizationLevel', 'size', 'parameterSize', 'format', 'family', 'digest'],
    'module': ['name', 'role', 'path', 'version', 'status', 'planned'],
    'note': ['noteType', 'isPinned'],
    'offer': ['price', 'currency', 'offerType', 'availability', 'bookingToken', 'departureToken', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'status', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'order': ['orderId', 'orderDate', 'total', 'totalAmount', 'originalTotal', 'originalTotalAmount', 'savings', 'currency', 'status', 'deliveryDate', 'eta', 'subtotal', 'tipAmount', 'deliveryFee', 'taxes', 'summary', 'fareBreakdown', 'deliveryInstructions', 'interactionType', 'orderUuid', 'body', 'head', 'messages', 'timeline', 'itemStates', 'latestArrival', 'progress', 'progressTotal', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'organization': ['industry', 'actorType'],
    'outcome': ['statement', 'status', 'priority', 'archived', 'metric', 'baseline', 'current', 'target'],
    'pass': ['status', 'quantity', 'purchasedQuantity', 'useCount', 'isAllDayPass', 'price', 'currency', 'ticketNumber', 'nameOnTicket', 'seatAssignment', 'boardingGroup', 'ticketClass', 'gate', 'terminal', 'checkinStatus', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'payment_method': ['identifier', 'type', 'subtype', 'brand', 'displayName', 'customDescription', 'holderName', 'last4', 'binRange', 'expMonth', 'expYear', 'expirationDate', 'currency', 'balance', 'fingerprint', 'isDefault', 'isPrimary', 'isExpired', 'isSelected', 'status', 'providerTokens', 'metadata'],
    'person': ['url', 'notes', 'about', 'actorType'],
    'persona': ['headline', 'who', 'goals', 'painPoints', 'reachesFor', 'quote'],
    'place': ['fullAddress', 'placeFormatted', 'streetNumber', 'street', 'neighborhood', 'locality', 'city', 'district', 'region', 'postalCode', 'country', 'countryCode', 'latitude', 'longitude', 'accuracy', 'featureType', 'categories', 'phone', 'website', 'hours', 'businessStatus', 'rating', 'reviewCount', 'priceLevel', 'timezone', 'eta', 'isOrderable', 'closedMessage', 'productCount', 'mapboxId', 'wikidataId', 'googlePlaceId'],
    'playlist': ['id', 'listId', 'listType', 'ordering_mode', 'member_shape', 'privacy', 'isDefault', 'isPublic', 'itemCount', 'arrangement', 'default_view', 'icon_size', 'sort_by', 'path'],
    'podcast': ['feedUrl'],
    'post': ['externalUrl', 'postType', 'score', 'commentCount', 'community'],
    'practice': ['description', 'code', 'codeSystem', 'aliases'],
    'principle': ['name', 'statement', 'rationale', 'domain', 'status'],
    'product': ['category', 'price', 'priceAmount', 'originalPrice', 'originalPriceAmount', 'currency', 'categories', 'availability', 'images', 'quantity', 'weight', 'weightValue', 'weightUnit', 'soldByWeight', 'department', 'aisle', 'sku', 'barcode', 'nutritionScore', 'novaGroup', 'calories', 'servingSize', 'customizationGroups'],
    'project': ['state', 'color', 'parentId'],
    'protocol': ['name', 'homepage', 'rfc', 'wikidataId'],
    'qualification': ['category', 'identifier', 'status', 'renewalPeriod', 'level', 'validIn', 'verificationUrl'],
    'quantity-kind': ['key', 'label'],
    'quote': ['context', 'year'],
    'repository': ['stars', 'forks', 'language', 'topics', 'openIssues', 'isArchived', 'isPrivate', 'defaultBranch', 'license', 'size'],
    'reservation': ['reservationType', 'reservationId', 'status', 'bookingType', 'bookingTime', 'modifiedTime', 'startTime', 'endTime', 'partySize', 'totalAmount', 'baseAmount', 'taxAmount', 'currency', 'checkinUrl', 'conditions', 'voidWindowEndsAt', 'availableActions', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'result': ['indexedAt', 'resultType', 'favicon', 'externalUrl', 'postId', 'score', 'similarity', 'community'],
    'review': ['rating', 'ratingMax', 'tags', 'isVerified', 'externalUrl', 'postType', 'score', 'commentCount', 'community'],
    'role': ['title', 'department', 'roleType', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'status', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'seatmap': ['flightNumber', 'origin', 'destination', 'fareBasisCode', 'classOfService', 'aircraftCode', 'totalSeats', 'availableSeats', 'cabins', 'tiers', 'hasExitRow', 'hasFreeSeats', 'hasPaidSeats', 'basicEconomyLocked'],
    'service': ['id', 'description', 'params', 'returns'],
    'settings': ['name'],
    'shape': ['plural', 'description', 'icon', 'fields', 'out', 'in', 'display', 'groups', 'identity', 'identity_any', 'also', 'derived', 'shortcuts', 'prior_art', 'prefsSchemas'],
    'shelf': ['isExclusive', 'id', 'listId', 'listType', 'ordering_mode', 'member_shape', 'privacy', 'isDefault', 'isPublic', 'itemCount', 'arrangement', 'default_view', 'icon_size', 'sort_by', 'path'],
    'software': ['version', 'applicationCategory', 'runtimePlatform', 'codename', 'category', 'price', 'priceAmount', 'originalPrice', 'originalPriceAmount', 'currency', 'categories', 'availability', 'images', 'quantity', 'weight', 'weightValue', 'weightUnit', 'soldByWeight', 'department', 'aisle', 'sku', 'barcode', 'nutritionScore', 'novaGroup', 'calories', 'servingSize', 'customizationGroups'],
    'sound': ['durationMs', 'channels', 'sampleRate', 'bitDepth', 'purpose', 'name', 'description', 'license', 'copyrightYear', 'datePublished', 'dateCreated', 'url', 'language', 'coverage', 'tags', 'filename', 'mimeType', 'size', 'path', 'format', 'encoding', 'lineCount', 'kind', 'sha'],
    'source': ['sourceId', 'address', 'scanner', 'enabled', 'description', 'lastSynced'],
    'spec': ['problem', 'successCriteria', 'remoteId', 'priority', 'state', 'labels', 'targetDate', 'target', 'parentId', 'projectId', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'status', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties', 'filename', 'mimeType', 'size', 'path', 'format', 'encoding', 'lineCount', 'kind', 'sha'],
    'subscription': ['app', 'op', 'target'],
    'symbol': ['urn', 'kind', 'lang', 'signature', 'summary', 'sourcePath', 'sourceLine'],
    'tag': ['color', 'tagType', 'annotated', 'hash'],
    'task': ['remoteId', 'priority', 'state', 'labels', 'targetDate', 'target', 'parentId', 'projectId', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'status', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'tax_line': ['code', 'description', 'amount', 'currency', 'kind', 'nature', 'country', 'appliesToIndex', 'refundable', 'merchantImposed', 'rate', 'taxableAmount', 'inclusive'],
    'theme': ['themeId', 'family', 'description', 'style', 'startMenu', 'defaultBackgroundColor'],
    'tool_call': ['name', 'input', 'output', 'isError', 'durationMs'],
    'transaction': ['amount', 'currency', 'balance', 'category', 'postingDate', 'pending', 'recurring', 'notes', 'type', 'details', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'status', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'transcript': ['language', 'languageConfidence', 'sourceType', 'contentRole', 'durationMs', 'segmentCount', 'segments'],
    'transition': ['givenName', 'additionalName', 'familyName', 'honorificPrefix', 'honorificSuffix', 'legalName', 'maidenName', 'sortAs', 'nameOrder', 'phoneticGivenName', 'phoneticFamilyName', 'gender', 'nickname', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'status', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'trip': ['tripType', 'status', 'departureTime', 'arrivalTime', 'duration', 'durationMinutes', 'distance', 'vehicleType', 'cabinClass', 'fare', 'fareAmount', 'currency', 'rating', 'trackingUrl', 'isSurge', 'isScheduled', 'stops', 'bookingToken', 'carbonEmissions', 'isPool', 'isReserve', 'guest', 'marketplace', 'vehicle', 'startDate', 'endDate', 'timezone', 'allDay', 'recurrence', 'visibility', 'showAs', 'dateUpdated', 'sourceUrl', 'sourceTitle', 'icalUid', 'distinctId', 'currentUrl', 'properties'],
    'unit': ['ucumCode', 'symbol', 'label', 'kind', 'siDigitalFrameworkUri', 'unCefactCommonCode', 'qudtUnitIri', 'wikidataId', 'toBaseFactor', 'toBaseOffset', 'iso4217', 'iso4217Numeric', 'minorExponent', 'logBase'],
    'user': ['osUsername', 'primaryUser', 'actorType'],
    'user_identity': ['user_id', 'volume_id', 'person_node_id', 'active'],
    'video': ['durationMs', 'resolution', 'frameRate', 'codec', 'viewCount', 'name', 'description', 'license', 'copyrightYear', 'datePublished', 'dateCreated', 'url', 'language', 'coverage', 'tags', 'filename', 'mimeType', 'size', 'path', 'format', 'encoding', 'lineCount', 'kind', 'sha'],
    'volume': ['volume_id', 'kind', 'source', 'address', 'provider', 'auto_mount', 'readOnly', 'removable', 'ejectable', 'totalBytes', 'freeBytes', 'scope', 'icon', 'default_view'],
    'vote': ['direction', 'note', 'instance'],
    'webpage': ['visitCount', 'lastVisitUnix', 'contentType', 'favicon', 'error'],
    'website': ['status', 'versionId', 'anonymous', 'claimToken', 'claimUrl'],
}

# Every shape whose `also:` chain includes `event` (plus `event` itself).
# Derived from the shape graph — the shape IS the type.
EVENT_TYPES: list[str] = [
    'activity',
    'birth',
    'booking_offer',
    'class',
    'conversion',
    'event',
    'flight',
    'git_commit',
    'health-condition',
    'health-immunization',
    'health-panel',
    'health-procedure',
    'health-reference-range',
    'insurance_policy',
    'invitation',
    'launch',
    'leg',
    'loaded_model',
    'measure',
    'meeting',
    'membership',
    'offer',
    'order',
    'pass',
    'reservation',
    'role',
    'spec',
    'task',
    'transaction',
    'transition',
    'trip',
]

# `derived:` bindings per shape — read-side resolver input.
# Binding grammar: {find, where, where_link, is, get} | {latest: [...]} | dotted string.
SHAPE_DERIVED: dict[str, dict] = {
    'issue': {'upvotes': {'count': 'for', 'where': {'direction': 'up'}}, 'downvotes': {'count': 'for', 'where': {'direction': 'down'}}, 'weight': {'tally': 'for', 'by': 'direction', 'map': {'up': 1, 'down': -1}}, 'status': {'reverse': 'addresses', 'get': 'status', 'prefer': ['achieved', 'active', 'at-risk', 'proposed'], 'map': {'achieved': 'addressed', 'active': 'in-progress', 'at-risk': 'in-progress', 'proposed': 'planned'}, 'default': 'open', 'authored': {'field': 'declined', 'equals': True, 'then': 'declined'}}},
    'person': {'birthdate': {'find': 'born_in', 'is': 'birth', 'get': 'startDate'}, 'current_residence': {'find': 'lived_at', 'where_link': {'to': None}, 'get': 'name'}, 'current_role': {'find': 'worked_at', 'where_link': {'to': None}, 'get': 'title'}, 'givenName': {'latest': [{'find': 'born_in', 'is': 'birth', 'get': 'givenName'}, {'find': 'changed', 'is': 'transition', 'get': 'givenName'}]}, 'additionalName': {'latest': [{'find': 'born_in', 'is': 'birth', 'get': 'additionalName'}, {'find': 'changed', 'is': 'transition', 'get': 'additionalName'}]}, 'familyName': {'latest': [{'find': 'born_in', 'is': 'birth', 'get': 'familyName'}, {'find': 'changed', 'is': 'transition', 'get': 'familyName'}]}, 'honorificPrefix': {'latest': [{'find': 'born_in', 'is': 'birth', 'get': 'honorificPrefix'}, {'find': 'changed', 'is': 'transition', 'get': 'honorificPrefix'}]}, 'honorificSuffix': {'latest': [{'find': 'born_in', 'is': 'birth', 'get': 'honorificSuffix'}, {'find': 'changed', 'is': 'transition', 'get': 'honorificSuffix'}]}, 'legalName': {'latest': [{'find': 'born_in', 'is': 'birth', 'get': 'legalName'}, {'find': 'changed', 'is': 'transition', 'get': 'legalName'}]}, 'maidenName': {'latest': [{'find': 'born_in', 'is': 'birth', 'get': 'maidenName'}, {'find': 'changed', 'is': 'transition', 'get': 'maidenName'}]}, 'sortAs': {'latest': [{'find': 'born_in', 'is': 'birth', 'get': 'sortAs'}, {'find': 'changed', 'is': 'transition', 'get': 'sortAs'}]}, 'nameOrder': {'latest': [{'find': 'born_in', 'is': 'birth', 'get': 'nameOrder'}, {'find': 'changed', 'is': 'transition', 'get': 'nameOrder'}]}, 'phoneticGivenName': {'latest': [{'find': 'born_in', 'is': 'birth', 'get': 'phoneticGivenName'}, {'find': 'changed', 'is': 'transition', 'get': 'phoneticGivenName'}]}, 'phoneticFamilyName': {'latest': [{'find': 'born_in', 'is': 'birth', 'get': 'phoneticFamilyName'}, {'find': 'changed', 'is': 'transition', 'get': 'phoneticFamilyName'}]}, 'gender': {'latest': [{'find': 'born_in', 'is': 'birth', 'get': 'gender'}, {'find': 'changed', 'is': 'transition', 'get': 'gender'}]}, 'nickname': {'latest': [{'find': 'born_in', 'is': 'birth', 'get': 'nickname'}, {'find': 'changed', 'is': 'transition', 'get': 'nickname'}]}},
}

# `shortcuts:` per shape — write-side flat-create expansion table.
# Each entry: flat_key -> {writes: <link>[is=<shape>].<field>}
SHAPE_SHORTCUTS: dict[str, dict] = {
    'person': {'birthdate': {'writes': 'born_in[is=birth].startDate'}, 'givenName': {'writes': 'born_in[is=birth].givenName'}, 'additionalName': {'writes': 'born_in[is=birth].additionalName'}, 'familyName': {'writes': 'born_in[is=birth].familyName'}, 'honorificPrefix': {'writes': 'born_in[is=birth].honorificPrefix'}, 'honorificSuffix': {'writes': 'born_in[is=birth].honorificSuffix'}, 'legalName': {'writes': 'born_in[is=birth].legalName'}, 'maidenName': {'writes': 'born_in[is=birth].maidenName'}, 'sortAs': {'writes': 'born_in[is=birth].sortAs'}, 'nameOrder': {'writes': 'born_in[is=birth].nameOrder'}, 'phoneticGivenName': {'writes': 'born_in[is=birth].phoneticGivenName'}, 'phoneticFamilyName': {'writes': 'born_in[is=birth].phoneticFamilyName'}, 'gender': {'writes': 'born_in[is=birth].gender'}, 'nickname': {'writes': 'born_in[is=birth].nickname'}},
}
